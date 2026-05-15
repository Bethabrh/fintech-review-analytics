import os
import pandas as pd

print("Current folder:", os.getcwd())
print("Files in raw folder:", os.listdir("data/raw"))

df = pd.read_csv("data/raw/raw_reviews.csv")
print(df.shape)
print(df.head())