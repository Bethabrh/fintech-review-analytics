import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/raw_reviews.csv")

print("Original shape:", df.shape)

# Remove duplicates
df_clean = df.drop_duplicates()

print("After removing duplicates:", df_clean.shape)

# Ensure no missing values
df_clean = df_clean.dropna()

# Normalize date format (safe conversion)
df_clean["date"] = pd.to_datetime(df_clean["date"], errors="coerce").dt.strftime("%Y-%m-%d")

# Save cleaned dataset
df_clean.to_csv("data/raw/raw_reviews.csv", index=False)

print("Clean dataset saved successfully!")