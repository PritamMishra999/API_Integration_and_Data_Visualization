import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# --- Configuration ---
COIN_ID = "bitcoin"  # You can change this to ethereum, solana, etc.
CURRENCY = "usd"
DAYS = 7

# --- API Request ---
url = f"https://api.coingecko.com/api/v3/coins/{COIN_ID}/market_chart"
params = {
    'vs_currency': CURRENCY,
    'days': DAYS
}

response = requests.get(url, params=params)

# Check if the request succeeded
if response.status_code != 200:
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

data = response.json()

# Check if 'prices' exists
if 'prices' not in data:
    raise KeyError("'prices' key not found in API response. Full response:\n" + str(data))

# --- Extract Data ---
timestamps = [datetime.fromtimestamp(item[0] / 1000) for item in data['prices']]
prices = [item[1] for item in data['prices']]

# --- Plotting ---
sns.set(style='darkgrid')
plt.figure(figsize=(14, 6))
plt.plot(timestamps, prices, color='blue', linewidth=2)

plt.title(f'{COIN_ID.capitalize()} Price in {CURRENCY.upper()} (Last {DAYS} Days)', fontsize=16)
plt.xlabel('Date & Time')
plt.ylabel(f'Price ({CURRENCY.upper()})')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
