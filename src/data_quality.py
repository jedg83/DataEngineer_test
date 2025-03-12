import pandas as pd

def check_data_quality(file_path):
    df = pd.read_csv(file_path)
    missing_values = df.isnull().sum().sum()
    
    if "price" in df.columns:
        outliers = df[(df["price"] > df["price"].quantile(0.99)) |
                      (df["price"] < df["price"].quantile(0.01))]

    print(f"Missing values: {missing_values}")
    print(f"Outliers detected: {len(outliers)}")

if __name__ == "__main__":
    check_data_quality("data/silver_real_time.csv")
    check_data_quality("data/silver_batch.csv")