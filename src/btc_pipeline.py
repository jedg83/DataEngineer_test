import pandas as pd

def ingest_batch_data():
    try:
        df = pd.read_csv("data/btc-news-recent-file.csv")  
        df.to_csv("data/bronze_batch.csv", index=False)
        print("Batch data stored in Bronze file.")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    ingest_batch_data()