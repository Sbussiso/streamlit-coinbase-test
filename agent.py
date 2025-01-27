import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from test import orderbook, historical_data, current_price
from langchain_core.tools import tool
from datetime import datetime

# Retrieve API keys from Streamlit secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]
tavily_api_key = st.secrets["TAVILY_API_KEY"]

# Ensure the variables are set
assert openai_api_key is not None, "OPENAI_API_KEY is not set in Streamlit secrets."
assert tavily_api_key is not None, "TAVILY_API_KEY is not set in Streamlit secrets."

llm = ChatOpenAI(model="gpt-4o", temperature=0)

search_tool = TavilySearchResults(max_results=2)

@tool
def orderbook_tool():
    """
    This tool returns the orderbook for BTC-USD
    """
    return orderbook()

@tool
def get_current_datetime():
    """
    This tool returns the current date and time.
    """
    return datetime.now().isoformat()

@tool
def historical_data_tool():
    """
    This tool returns the historical data for BTC-USD
    """
    return historical_data()

@tool
def current_price_tool():
    """
    This tool returns the current price for BTC-USD
    """
    return current_price()

# Updated tools list to include the new date and time tool
tools = [search_tool, orderbook_tool, get_current_datetime, historical_data_tool, current_price_tool]

# Initialize the agent with the updated tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Now you can run the agent directly
def ask_agent(query):
    return agent.run(query)

# Example usage
if __name__ == '__main__':
    user_query = "What is the current date and time?"
    result = ask_agent(user_query)
    print("Agent's Response:")
    print(result)
    