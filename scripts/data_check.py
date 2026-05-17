import pandas as pd
import os

file_path = "data/raw/raw_reviews.csv"

print("Checking dataset...")

df = pd.read_csv(file_path)

print("\nShape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())

print("\nSample data:")
print(df.head())