import requests
import pandas as pd
import time
from datetime import datetime

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def fetch_real_time_data():
    try:
        response = requests.get(BINANCE_URL)
        data = response.json()  # Convert response to JSON

        # Print the full response for debugging
        print("API Response:", data)  

        # Check if expected keys exist
        if not isinstance(data, dict) or "symbol" not in data or "price" not in data:
            raise KeyError(f"Unexpected API response format: {data}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Convert data to DataFrame
        df = pd.DataFrame([[timestamp, data["symbol"], data["price"]]],
                          columns=["timestamp", "symbol", "price"])

        # Append to Bronze CSV
        df.to_csv("data/bronze_real_time.csv", mode="a", header=False, index=False)
        print(f"Data stored at {timestamp}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    while True:
        fetch_real_time_data()
        time.sleep(30)  # Fetch every 30 seconds
