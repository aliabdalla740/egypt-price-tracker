import sqlite3

conn = sqlite3.connect("prices.db")
for row in conn.execute("SELECT * FROM usd_egp"):
    print(row)
conn.close()