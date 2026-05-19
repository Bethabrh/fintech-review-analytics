# Fintech Mobile Banking Analytics Report

## 1. Executive Summary
This project analyzes Google Play Store reviews for CBE, BOA, and Dashen Bank apps to identify user sentiment, key pain points, and improvement opportunities.

## 2. Methodology
- Data scraped using google-play-scraper
- Sentiment analysis using DistilBERT
- Theme extraction using TF-IDF + rule-based classification

## 3. Key Findings
- Transaction delays are the most common complaint across all banks
- BOA has the highest negative sentiment rate
- Dashen has the best UI feedback but still suffers stability issues

## 4. Visual Insights
(Insert plots here)

## 5. Recommendations
- Improve backend transaction performance
- Fix authentication systems (OTP/login)
- Invest in stability improvements for BOA

## 6. Limitations
- Google Play bias (only unhappy users tend to review)
- Rule-based theme classification
- Limited to English reviews