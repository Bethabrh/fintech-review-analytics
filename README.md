📊 FinTech Review Analytics Pipeline
📌 Project Overview

This project implements an end-to-end data analytics pipeline for fintech mobile banking app reviews collected from the Google Play Store. It transforms raw user feedback into structured insights using data engineering and NLP techniques.

The goal is to analyze customer sentiment and extract recurring themes from Ethiopian banking apps:

Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank

The final output helps identify user satisfaction drivers, pain points, and product improvement opportunities.

🏗️ Project Structure
fintech-review-analytics/
│
├── data/
│   └── raw/
│       ├── raw_reviews.csv
│       ├── clean_reviews.csv
│       ├── reviews_with_sentiment.csv
│       └── reviews_with_themes.csv
│
├── src/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_analysis.py
│   └── theme_extraction.py
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── requirements.txt
└── README.md
⚙️ Pipeline Workflow

The project follows a structured pipeline:

Data Collection → Data Cleaning → Sentiment Analysis → Theme Extraction

📥 Task 1: Data Scraping

File: src/scrape_reviews.py

Functionality:
Scrapes Google Play Store reviews using google-play-scraper
Targets Ethiopian banking apps:
CBE
BOA
Dashen Bank
Extracts:
Review text
Rating (1–5)
Date
Bank name
Source (Google Play)
Output:
data/raw/raw_reviews.csv
🧹 Task 2.1: Data Preprocessing

File: src/preprocess_reviews.py

Steps:
Remove duplicate reviews
Handle missing values
Standardize date format (YYYY-MM-DD)
Clean text (remove extra spaces and noise)
Output:
data/raw/clean_reviews.csv
💬 Task 2.2: Sentiment Analysis

File: src/sentiment_analysis.py

Model Used:
distilbert-base-uncased-finetuned-sst-2-english
Functionality:
Classifies reviews as:
Positive
Negative
Generates confidence score for each prediction
Output:
data/raw/reviews_with_sentiment.csv
🧠 Task 2.3: Theme Extraction

File: src/theme_extraction.py

Method:
TF-IDF vectorization (keyword extraction)
Rule-based classification
Themes Identified:
Transaction Performance
App Stability
User Interface
Account Access Issues
Feature Requests
General Feedback
Output:
data/raw/reviews_with_themes.csv
📊 Key Insights
Majority of reviews fall under General Feedback
Major issues identified:
Transaction delays
Login/authentication failures
App crashes and instability
Positive feedback highlights:
Ease of use
Mobile banking convenience
🚀 How to Run the Project
pip install -r requirements.txt

python src/scrape_reviews.py
python src/preprocess_reviews.py
python src/sentiment_analysis.py
python src/theme_extraction.py
⚠️ Limitations
Sentiment model is not trained on Ethiopian banking-specific data
Theme classification is rule-based (not a trained ML model)
Dataset is limited to Google Play Store reviews only
📌 Technologies Used
Python
pandas
scikit-learn
HuggingFace Transformers
google-play-scraper
👨‍💻 Author

FinTech Review Analytics Project

🧠 Summary

This project demonstrates a complete data engineering + NLP pipeline that transforms raw fintech app reviews into structured insights for product decision-making.