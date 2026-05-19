import pandas as pd
import psycopg2

# -----------------------------
# CONNECT TO POSTGRESQL
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
   password="Fintech@2026_DB!"
)

cursor = conn.cursor()

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("data/raw/reviews_with_themes.csv")

print("Dataset loaded successfully!")

# -----------------------------
# INSERT UNIQUE BANKS
# -----------------------------
banks = df["bank"].unique()

for bank in banks:
    cursor.execute(
        """
        INSERT INTO banks (bank_name)
        VALUES (%s)
        ON CONFLICT (bank_name) DO NOTHING
        """,
        (bank,)
    )

conn.commit()

print("Banks inserted!")

# -----------------------------
# FETCH BANK IDs
# -----------------------------
cursor.execute("SELECT bank_id, bank_name FROM banks")

bank_rows = cursor.fetchall()

bank_map = {}

for row in bank_rows:
    bank_map[row[1]] = row[0]

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

print("Reviews inserted successfully!")

cursor.close()
conn.close()

print("Database loading completed!")