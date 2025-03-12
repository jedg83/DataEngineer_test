import pandas as pd

def ingest_batch_data():
    try:
        df = pd.read_csv("data/historical_btc.csv")  # Replace with your actual file
        df.to_csv("data/bronze_batch.csv", index=False)
        print("Batch data stored in Bronze layer.")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    ingest_batch_data()