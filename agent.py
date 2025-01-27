import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from test import orderbook

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
tavily_api_key = os.getenv('TAVILY_API_KEY')

# Ensure the variables are set
assert openai_api_key is not None, "OPENAI_API_KEY is not set in the .env file."
assert tavily_api_key is not None, "TAVILY_API_KEY is not set in the .env file."

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

search_tool = TavilySearchResults(max_results=2)

orderbook_tool = orderbook()

tools = [search_tool, orderbook_tool]

# Instead of create_openai_functions_agent, use initialize_agent
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
    user_query = "What is LangChain?"
    result = ask_agent(user_query)
    print("Agent's Response:")
    print(result)
    