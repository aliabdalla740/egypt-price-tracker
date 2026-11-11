# Egypt Price Tracker

A small data engineering project that collects the USD to EGP exchange rate
and stores it in a database, so we can track how it changes over time.

## What it does

1. Fetches the latest USD to EGP rate from a public API.
2. Stores each reading in a SQLite database.

## Tech stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## Coming soon

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

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
- [ ] Build a Power BI dashboard