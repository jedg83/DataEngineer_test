import streamlit as st
import pandas as pd
import time

st.title("BTC/USD Market Data Dashboard")

def load_data():
    df = pd.read_csv("data/gold_real_time.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    st.line_chart(df[["price"]])
    return df

placeholder = st.empty()




#while True:
data = load_data()
    
   
#    placeholder.dataframe(data.tail(10))
    
    
#    st.line_chart(data.set_index("timestamp")["price"])
    
#    time.sleep(10)