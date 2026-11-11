# Egypt Price Tracker

A small data engineering project that collects the USD to EGP exchange rate
and stores it in a database, so we can track how it changes over time.

## What it does

1. Fetches the latest USD to EGP rate from a public API.
2. Stores each reading in a SQLite database.

## Tech stack

- Python
- SQLite
- Git and GitHub

## How to run

```
python -m venv venv
venv\Scripts\activate
pip install requests
python fetch_prices.py
python check_db.py
```

## Roadmap

- [x] Fetch USD to EGP rate
- [x] Store it in SQLite
- [ ] Add gold prices
- [ ] Move to PostgreSQL and Docker
- [ ] Schedule daily runs with Airflow
- [ ] Build a dashboard