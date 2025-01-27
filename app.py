import streamlit as st
import pandas as pd
import numpy as np
from test import current_price, orderbook, historical_data
import plotly.graph_objects as go
from agent import ask_agent

from streamlit_extras.metric_cards import style_metric_cards

# Initialize chat_history in session_state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

with st.sidebar:

    st.title("Order Panel")

    # Create a select box to choose which orders to display
    order_book = orderbook()
    st.write(order_book)
    prompt = "Identify trends in the real Bitcoin orderbook that are relevant to crypto trading. You are not a teacher, you only point out trends in the data."
    if prompt:
        result = ask_agent(prompt)
        st.write("Agent's Response:")
        st.write(result)

st.title("Coinbase Trader")
st.subheader("Automatically buy and sell bitcoin")
st.markdown("---")
st.subheader("Price Action")

# Create a select box to choose which orders to display
view_option = st.selectbox(
    "Select an Order View",
    ("Line Graph", "Candle Graph")
)

# Depending on the user's selection, show the appropriate content
if view_option == "Line Graph":
    st.write("buy form here")
    
    data = historical_data()
    chart_data = pd.DataFrame(data)

    # Use the columns of the data as options for the multiselect
    options = st.multiselect(
        "Select lines to display",
        chart_data.columns.tolist(),
        chart_data.columns.tolist()  # Default to all columns selected
    )

    st.write("You selected:", options)

    data_range = st.slider("Data Range", 0, len(chart_data), 25)
    st.write("Data Range", data_range)
    
    # Filter the data based on selected options and data range
    filtered_data = chart_data[options].iloc[-data_range:]

    # Display the line chart with the filtered data
    st.line_chart(filtered_data)


elif view_option == "Candle Graph":
    # Fetch data
    data = historical_data()

    # Streamlit app
    st.title('Bitcoin Candlestick Chart')

    # Plotly candlestick chart with customized colors
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        increasing_line_color='green',  # Positive candles
        decreasing_line_color='red'     # Negative candles
    )])

    fig.update_layout(
        title='BTC-USD Candlestick Chart',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig)

st.subheader(f"Current Price: {current_price()} USD")
    

# Create a select box to choose which orders to display
view_option = st.selectbox(
    "Select an Order View",
    ("Dashboard", "CoinBot")
)
    

if view_option == "Dashboard":
    
    col1, col2 = st.columns(2)

    col1.metric(label="Total Gain", value=5000, delta=1000)
    col2.metric(label="Total Loss", value=5000, delta=-1000)

    style_metric_cards()


if view_option == "CoinBot":

    st.title("Chat with Bot")
    prompt = st.chat_input("How has bitcoin been performing this week?")
    if prompt:
        # Append user input to chat history
        st.session_state['chat_history'].append({"role": "User", "content": prompt})
        
        # Get agent response
        result = ask_agent(prompt)
        
        # Append agent response to chat history
        st.session_state['chat_history'].append({"role": "Agent", "content": result})
    
    # Display the chat history with better formatting
    for chat in st.session_state['chat_history']:
        if chat["role"] == "User":
            st.markdown(f"<div style='text-align: right;'><b>User:</b> {chat['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left;'><b>Agent:</b> {chat['content']}</div>", unsafe_allow_html=True)
