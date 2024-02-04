import streamlit as st
import pandas as pd
import yfinance as yf

#loading for cache_resource
#else for cache_data

@st.cache_data
def load_data(filename):
  return pd.read_csv(filename)

df = load_data("data//salary_data.csv")
st.write(df.head())


@st.cache_resource(ttl=60)  # Cache for 60 seconds
def fetch_stock_data(symbol):
  return yf.download(symbol, period="1d", interval="5m")

symbol = st.sidebar.text_input("Enter Stock Symbol")

if symbol:
  data = fetch_stock_data(symbol)
  st.write(f"Current Price: {data['Close'][-1]}")
  st.line_chart(data["Close"])
