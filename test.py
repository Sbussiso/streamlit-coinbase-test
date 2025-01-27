import streamlit as st
import requests
import json
import pandas as pd
import http
import plotly.graph_objects as go
import http.client

def current_price():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)
    data = response.json()
    price = data['data']['amount']
    return price

@st.cache_data
def orderbook():
    # Set up a connection to the Coinbase API
    conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Python http.client'  # It's good practice to set a User-Agent
    }

    # The product_id for Bitcoin
    product_id = 'BTC-USD'

    # Request the order book
    conn.request("GET", f"/products/{product_id}/book?level=2", '', headers)

    res = conn.getresponse()
    data = res.read()

    # Decode the response data
    order_book = json.loads(data.decode("utf-8"))

    # Convert the order book data to Pandas DataFrames
    bids_df = pd.DataFrame(order_book['bids'], columns=['price', 'size', 'num_orders'])
    asks_df = pd.DataFrame(order_book['asks'], columns=['price', 'size', 'num_orders'])

    # Optionally, you can convert the price and size to numeric types for further analysis
    bids_df['price'] = pd.to_numeric(bids_df['price'])
    bids_df['size'] = pd.to_numeric(bids_df['size'])
    asks_df['price'] = pd.to_numeric(asks_df['price'])
    asks_df['size'] = pd.to_numeric(asks_df['size'])

    # Combine bids and asks into one DataFrame
    bids_df['type'] = 'bid'
    asks_df['type'] = 'ask'
    order_book_df = pd.concat([bids_df, asks_df])
    return order_book_df

# Function to fetch historical crypto data
@st.cache_data
def historical_data():
    product_id = 'BTC-USD'
    conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Python http.client'
    }
    conn.request("GET", f"/products/{product_id}/candles?granularity=3600", '', headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)
    df = df.sort_index()
    
    return df

