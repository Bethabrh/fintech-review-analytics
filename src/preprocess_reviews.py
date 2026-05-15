import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/raw_reviews.csv")

print("Original shape:", df.shape)

# ----------------------------
# 1. Remove duplicates
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# 2. Remove missing values
# ----------------------------
df = df.dropna(subset=["review", "rating"])

# ----------------------------
# 3. Normalize date format
# ----------------------------
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# ----------------------------
# 4. Basic cleaning of text
# ----------------------------
df["review"] = df["review"].str.strip()

# ----------------------------
# 5. Final check
# ----------------------------
print("Cleaned shape:", df.shape)

# ----------------------------
# Save cleaned dataset
# ----------------------------
df.to_csv("data/raw/clean_reviews.csv", index=False)

print("Clean dataset saved successfully!")