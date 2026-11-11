import sqlite3
import requests

URL = "https://open.er-api.com/v6/latest/USD"
DB_NAME = "prices.db"


def fetch_rate():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["rates"]["EGP"], data["time_last_update_utc"]


def save_rate(rate, api_updated_at):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usd_egp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rate REAL,
            api_updated_at TEXT,
            fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute(
        "INSERT INTO usd_egp (rate, api_updated_at) VALUES (?, ?)",
        (rate, api_updated_at),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    rate, updated = fetch_rate()
    save_rate(rate, updated)
    print(f"Saved: 1 USD = {rate} EGP")