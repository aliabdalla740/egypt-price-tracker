import requests

URL = "https://open.er-api.com/v6/latest/USD"

response = requests.get(URL, timeout=10)
response.raise_for_status()

data = response.json()

egp = data["rates"]["EGP"]

print(f"1 USD = {egp} EGP")
print("Last update:", data["time_last_update_utc"])