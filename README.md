# API_Integration_and_Data_Visualization

This Python application fetches real-time cryptocurrency price data from the CoinGecko API and visualizes it using Matplotlib and Seaborn. The current configuration displays the past 7 days of Bitcoin price trends in USD.

🚀 Features

📡 Integrates with CoinGecko API for real-time cryptocurrency data.
📊 Plots clean, informative price trend graphs using Matplotlib and Seaborn.
🛠 Easy customization to track different coins, currencies, and timeframes.

📂 File Structure
app.py: Main script for fetching data and generating visualizations.

🔧 Configuration
Modify these variables at the top of app.py to customize:
COIN_ID = "bitcoin"      # e.g., "ethereum", "solana", etc.
CURRENCY = "usd"         # e.g., "eur", "inr", etc.
DAYS = 7                 # Number of past days to visualize

📦 Requirements
1. Python 3.x
2. requests
3. matplotlib
4. seaborn

Install dependencies using pip:
pip install requests matplotlib seaborn

▶️ Usage
Run the script:
python app.py
This will:

1. Fetch price data from the CoinGecko API.
2. Parse and process the time-series data.
3. Display a line chart showing price trends.

📈 Output
The script outputs a time-series plot of the selected cryptocurrency’s price over the past specified number of days.

🧩 Notes
Ensure you have an active internet connection.

CoinGecko's public API is rate-limited — avoid excessive requests.

📃 License
This project is open-source and available under the MIT License.
