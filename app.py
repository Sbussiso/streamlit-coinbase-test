import streamlit as st
import pandas as pd
import numpy as np
from test import current_price, orderbook, historical_data
import plotly.graph_objects as go


from streamlit_extras.metric_cards import style_metric_cards

with st.sidebar:
    st.title("Trade Panel")
    
    
    # Create a select box to choose which orders to display
    view_option = st.selectbox(
        "Select an Order View",
        ("Buy", "Sell", "Cancel Order")
    )

    # Depending on the user's selection, show the appropriate content
    if view_option == "Buy":
        
        with st.form("my_form"):
            st.write("Buy Here")

            number = st.number_input("Insert a number")
            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("USD", number)
                st.write("BTC", number) #TODO
            


    elif view_option == "Sell":
        st.write("sell form here")
    
    elif view_option == "Cancel Order":
        st.write("cancel order form")

    st.markdown("---")

    st.title("Orders")
    # Create a select box to choose which orders to display
    order_book = orderbook()
    st.write(order_book)
    
            
        



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
    options = st.multiselect(
        "What are your favorite colors",
        ["Green", "Yellow", "Red", "Blue"],
        ["Yellow", "Red"],
    )

    st.write("You selected:", options)
    
    data = historical_data()

    # Generate random data with 20 rows and 3 columns
    chart_data = pd.DataFrame(data)

    # Display the line chart
    st.line_chart(chart_data)


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
    ("Gains/Losses")
)

    
if view_option == "Gains/Losses":
    
    
    col1, col2 = st.columns(2)

    col1.metric(label="Total Gain", value=5000, delta=1000)
    col2.metric(label="Total Loss", value=5000, delta=-1000)

    style_metric_cards()
    
