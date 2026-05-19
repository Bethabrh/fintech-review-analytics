import pandas as pd
import psycopg2

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="YOUR_PASSWORD"
)

cursor = conn.cursor()

# -----------------------------
# LOAD CSV
# -----------------------------
df = pd.read_csv("data/raw/reviews_with_themes.csv")

# -----------------------------
# INSERT BANKS
# -----------------------------
banks = df["bank"].unique()

for bank in banks:
    cursor.execute(
        """
        INSERT INTO banks (bank_name)
        VALUES (%s)
        ON CONFLICT DO NOTHING
        """,
        (bank,)
    )

conn.commit()

# -----------------------------
# CREATE BANK ID MAP
# -----------------------------
cursor.execute("SELECT bank_id, bank_name FROM banks")
bank_rows = cursor.fetchall()

bank_map = {name: bank_id for bank_id, name in bank_rows}

# -----------------------------
# INSERT REVIEWS
# -----------------------------
for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            bank_map[row["bank"]],
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["theme"],
            row["source"]
        )
    )

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()