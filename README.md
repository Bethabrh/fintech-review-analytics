# 🧠 Pipeline Overview

This project is divided into two main phases:

## Task 1: Data Collection & Preprocessing
- scrape_reviews.py → Scrapes Google Play reviews for CBE, BOA, Dashen
- preprocess_reviews.py → Cleans dataset (duplicates, missing values, date formatting)
- Output: data/raw/raw_reviews.csv (1200 reviews)

## Task 2: NLP Analysis
- sentiment_analysis.py → Applies DistilBERT sentiment classification
- theme_extraction.py → Extracts keywords and clusters into themes using TF-IDF

## Dataset Summary
- Total reviews: 1200+
- Banks: CBE, BOA, Dashen
- Source: Google Play Store
# ▶️ How to Run Project

## Task 1: Scraping + Preprocessing
python src/scrape_reviews.py
python src/preprocess_reviews.py

## Task 2: Sentiment Analysis
python src/sentiment_analysis.py

## Task 2: Theme Extraction
python src/theme_extraction.py
