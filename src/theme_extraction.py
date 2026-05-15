import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# -----------------------------
# CLEANING FUNCTION (IMPORTANT)
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)  # remove numbers & emojis
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["clean_review"] = df["review"].apply(clean_text)

# -----------------------------
# TF-IDF (IMPROVED)
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 3),   # important upgrade
    min_df=2,             # ignore rare noise words
    max_df=0.8,           # ignore too common words
    max_features=30
)

X = vectorizer.fit_transform(df["clean_review"])

keywords = vectorizer.get_feature_names_out()

print("\n=== TOP FEATURES (IMPROVED THEMES) ===")
for k in keywords:
    print("-", k)

# -----------------------------
# BUSINESS THEME RULES (UPGRADED)
# -----------------------------
def assign_theme(text):
    text = text.lower()

    if any(x in text for x in ["login", "log in", "otp", "password", "sign"]):
        return "Account Access Issues"

    elif any(x in text for x in ["slow", "delay", "transfer", "transaction", "payment"]):
        return "Transaction Performance"

    elif any(x in text for x in ["crash", "error", "bug", "freeze", "not working"]):
        return "App Stability"

    elif any(x in text for x in ["ui", "interface", "design", "layout"]):
        return "User Interface"

    elif any(x in text for x in ["feature", "fingerprint", "face id", "dark mode"]):
        return "Feature Requests"

    else:
        return "General Feedback"

df["theme"] = df["clean_review"].apply(assign_theme)

# -----------------------------
# SAVE OUTPUT
# -----------------------------
output_path = "data/raw/reviews_with_themes.csv"
df.to_csv(output_path, index=False)

print("\nTheme distribution:")
print(df["theme"].value_counts())

print("\nSaved to:", output_path)