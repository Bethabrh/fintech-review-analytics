from google_play_scraper import reviews, Sort
import pandas as pd
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

TOTAL_REVIEWS_PER_BANK = 400


# -----------------------------
# SCRAPER FUNCTION
# -----------------------------
def scrape_bank_reviews(bank_name, app_id, count=400):
    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=count
    )

    data = []

    for r in result:
        data.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        })

    return data


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    all_data = []

    for bank, app_id in BANK_APPS.items():
        print(f"Scraping {bank}...")

        reviews_data = scrape_bank_reviews(bank, app_id, TOTAL_REVIEWS_PER_BANK)
        all_data.extend(reviews_data)

        print(f"{bank}: {len(reviews_data)} reviews collected")

    df = pd.DataFrame(all_data)

    # Create folder safely
    os.makedirs("data/raw", exist_ok=True)

    # Save file
    df.to_csv("data/raw/raw_reviews.csv", index=False)

    print("\nDone!")
    print(df.head())


if __name__ == "__main__":
    main()