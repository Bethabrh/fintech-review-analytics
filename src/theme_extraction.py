import pandas as pd
 main
from transformers import pipeline

# Load cleaned data
df = pd.read_csv("data/raw/clean_reviews.csv")

# Load sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiments = []
scores = []

for review in df["review"]:
    result = classifier(str(review))[0]

    label = result["label"]
    score = result["score"]

    # Normalize labels
    if label == "POSITIVE":
        sentiments.append("positive")
    else:
        sentiments.append("negative")

    scores.append(score)

# Add to dataframe
df["sentiment_label"] = sentiments
df["sentiment_score"] = scores

# Save result
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print(df[["review", "sentiment_label", "sentiment_score"]].head())
print("\nSentiment analysis completed!")

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
 task-1
