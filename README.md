# API_Integration_and_Data_Visualization

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PRITAM PRIYADARSHI MISHRA

*INTERN ID*: CT04DN505

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

📘DESCRIPTION/OVERVIEW

The API Integration and Data Visualization application is a Python-based tool designed to fetch real-time cryptocurrency price data using the CoinGecko API and present it in a visually insightful format. This lightweight yet powerful script allows users to retrieve historical price data of a selected cryptocurrency over a defined number of past days and automatically generate an interactive line chart illustrating the price trend. It is a helpful utility for developers, traders, analysts, and educators who wish to explore or demonstrate how to integrate APIs with data visualization in Python.

🚀 Features

API Integration: The script uses the CoinGecko API to fetch up-to-date market data.
Customizable Parameters: Users can specify which cryptocurrency to analyze, the currency to display prices in, and the number of days to visualize.
Data Parsing: Extracts timestamps and price values from the API’s JSON response.
Graphical Representation: Uses matplotlib and seaborn to plot a line graph for intuitive and easy-to-read visualization.
Error Handling: Includes robust handling for potential issues such as failed API requests or malformed responses.

📂 Project Structure
The project consists of a single Python script:
app.py — The main script containing all logic for API calls, data processing, and plotting.

🔧 Configuration
The application is fully configurable through simple variables defined at the beginning of the app.py script. You can modify the following parameters to tailor the data retrieval and visualization:
COIN_ID = "bitcoin"      # e.g., "ethereum", "solana", etc.
CURRENCY = "usd"         # e.g., "eur", "inr", etc.
DAYS = 7                 # Number of past days to visualize
By changing these values, the app can be repurposed for different cryptocurrencies, currencies, or time spans without modifying the core logic.

📦 Requirements
1. Python 3.x
2. requests
3. matplotlib
4. seaborn

Install dependencies using pip:
pip install requests matplotlib seaborn

▶️ Usage
This will execute the following steps:
1. Send a GET request to the CoinGecko API to fetch the price data for the specified coin.
2. Extract the time-series data from the JSON response.
3. Convert UNIX timestamps to human-readable datetime objects.
4. Plot the data using matplotlib and seaborn with a visually appealing dark grid style.
5. Display a responsive graph showing how the price of the selected cryptocurrency has changed over time.

📊 Output Visualization
The final output is a time-series line chart with:
1. A clean, labeled X-axis showing date and time.
2. A Y-axis indicating the price in the selected currency.
3. A title summarizing the data context (coin, currency, and time period).
4. Gridlines and axis labels for improved readability.
![image](https://github.com/user-attachments/assets/9cb8fab6-91da-47b6-a485-310f9450705e)


🚨 Error Handling
The script includes checks to ensure a successful API response. If the API call fails or the expected data format is not received, meaningful error messages will be printed, preventing crashes and aiding in debugging.

🔍 Use Cases
1. Demonstrate API integration and data visualization in coding tutorials or classrooms.
2. Build foundational tools for crypto price monitoring.
3. Extend it into a larger dashboard or analytics system.
4. Use it for data collection and research purposes.

🧩 Notes
Ensure you have an active internet connection.
CoinGecko's public API is rate-limited — avoid excessive requests.

📃 License
This project is distributed under the MIT License, meaning it is free to use, modify, and distribute with appropriate attribution.
