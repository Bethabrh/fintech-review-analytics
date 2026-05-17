# FinTech Review Analytics Pipeline

## 📌 Project Overview
This project implements an end-to-end data analytics pipeline for fintech mobile banking app reviews collected from the Google Play Store. The system performs scraping, preprocessing, sentiment analysis, and theme extraction to understand user feedback across Ethiopian banking applications.

The goal is to extract actionable insights from customer reviews of mobile banking apps such as Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank.

---

## 🏗️ Project Structure

```
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
├── scripts/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Workflow

The project follows a structured pipeline:

**Data Collection → Data Cleaning → Sentiment Analysis → Theme Extraction**

---

## 📥 Task 1: Data Scraping

**File:** `src/scrape_reviews.py`

- Scrapes Google Play Store reviews using `google-play-scraper`
- Targets Ethiopian banking apps:
  - Commercial Bank of Ethiopia (CBE)
  - Bank of Abyssinia (BOA)
  - Dashen Bank
- Extracted fields:
  - Review text
  - Rating
  - Date
  - Bank name

Output: `data/raw/raw_reviews.csv`

---

## 🧹 Task 2.1: Data Preprocessing

**File:** `src/preprocess_reviews.py`

- Removes duplicate records
- Handles missing values
- Standardizes date format
- Cleans review text (removes extra spaces and noise)

Output: `data/raw/clean_reviews.csv`

---

## 💬 Task 2.2: Sentiment Analysis

**File:** `src/sentiment_analysis.py`

- Uses HuggingFace Transformer model:
  - `distilbert-base-uncased-finetuned-sst-2-english`
- Classifies reviews into:
  - Positive
  - Negative
- Produces confidence scores for predictions

Output: `data/raw/reviews_with_sentiment.csv`

---

## 🧠 Task 2.3: Theme Extraction

**File:** `src/theme_extraction.py`

- Applies TF-IDF vectorization to extract keywords
- Uses rule-based logic to categorize themes:
  - Transaction Performance
  - App Stability
  - User Interface
  - Account Access Issues
  - Feature Requests
  - General Feedback

Output: `data/raw/reviews_with_themes.csv`

---

## 📊 Key Insights

- Most reviews fall under general feedback
- Common issues:
  - Transaction delays
  - Login and authentication problems
  - App crashes and instability
- Positive feedback includes:
  - Ease of use
  - Mobile banking convenience

---

## 🚀 How to Run

```bash
pip install -r requirements.txt

python src/scrape_reviews.py
python src/preprocess_reviews.py
python src/sentiment_analysis.py
python src/theme_extraction.py
```

---

## ⚠️ Limitations

- Sentiment model is not trained on Ethiopian banking-specific data
- Theme classification is rule-based, not a trained ML classifier
- Dataset is limited to Google Play Store reviews only

---

## 📌 Technologies Used

- Python
- pandas
- scikit-learn
- HuggingFace Transformers
- google-play-scraper

---

## 👨‍💻 Author
FinTech Review Analytics Project