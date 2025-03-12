import pandas as pd

def cleaning_data(file_path, output_path):
    df = pd.read_csv(file_path)
    
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    
    df["price"] = df["price"].astype(float)
    
    
    df.drop_duplicates(inplace=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data stored in {output_path}")

if __name__ == "__main__":
    cleaning_data("data/bronze_real_time.csv", "data/silver_real_time.csv")
    cleaning_data("data/bronze_batch.csv", "data/silver_batch.csv")