import pandas as pd

def aggregate_gold_data(input_path, output_path):
    df = pd.read_csv(input_path)


    df["timestamp"] = pd.to_datetime(df["timestamp"])

    
    df["moving_avg"] = df["price"].rolling(window=5, min_periods=1).mean()


    df.to_csv(output_path, index=False)
    print(f"Aggregated data stored in {output_path}")

aggregate_gold_data("data/silver_real_time.csv", "data/gold_real_time.csv")