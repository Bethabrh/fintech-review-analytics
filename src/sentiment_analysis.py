import pandas as pd
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