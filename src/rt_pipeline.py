import requests
import pandas as pd
import time
from datetime import datetime

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def fetch_real_time_data():
    try:
        response = requests.get(COINGECKO_URL)
        data = response.json()  

        print("API Response:", data)  # Debugging 

       
        if "bitcoin" not in data or "usd" not in data["bitcoin"]:
            raise KeyError(f"Error Unexpected API response format: {data}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        price = data["bitcoin"]["usd"]

        
        df = pd.DataFrame([[timestamp, "BTC/USD", price]],
                          columns=["timestamp", "symbol", "price"])

       
        df.to_csv("data/bronze_real_time.csv", mode="a", header=False, index=False)
        print(f"Data stored at {timestamp}: BTC/USD = ${price}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    while True:
        fetch_real_time_data()
        time.sleep(30)  # every 30 seconds
