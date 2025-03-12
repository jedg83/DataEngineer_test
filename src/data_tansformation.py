import pandas as pd

def cleaning_data_rt(file_path, output_path):
    df = pd.read_csv(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = df["price"].astype(float)
    df.drop_duplicates(inplace=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data stored in {output_path}")

def cleaning_data_btc(file_path, output_path):
    df = pd.read_csv(file_path)
    df["published_date"] = pd.to_datetime(df["published_date"])
    df["_score"] = df["_score"].astype(float)
    df.drop_duplicates(inplace=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data stored in {output_path}")

if __name__ == "__main__":
    cleaning_data_rt("data/bronze_real_time.csv", "data/silver_real_time.csv")
    cleaning_data_btc("data/bronze_batch.csv", "data/silver_batch.csv")