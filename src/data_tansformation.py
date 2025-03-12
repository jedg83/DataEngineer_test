import pandas as pd

def clean_data(file_path, output_path):
    df = pd.read_csv(file_path)
    
    # Convert timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # Convert price to float
    df["price"] = df["price"].astype(float)
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data stored in {output_path}")

if __name__ == "__main__":
    clean_data("data/bronze_real_time.csv", "data/silver_real_time.csv")
    clean_data("data/bronze_batch.csv", "data/silver_batch.csv")