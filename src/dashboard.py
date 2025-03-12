import streamlit as st
import pandas as pd
import time

st.title("BTC/USD Market Data Dashboard")

# Load Data
def load_data():
    df = pd.read_csv("data/gold_real_time.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

placeholder = st.empty()

while True:
    data = load_data()
    
    # Display latest data
    placeholder.dataframe(data.tail(10))
    
    # Line chart for BTC prices
    st.line_chart(data.set_index("timestamp")["price"])
    
    time.sleep(10)