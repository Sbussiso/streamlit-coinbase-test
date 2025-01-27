# Crypto Trading Bot and Analysis Tool

This project is a comprehensive solution for cryptocurrency trading and analysis, with a focus on the Coinbase exchange. It includes various components such as an agent or bot for automated trading, a web application for data visualization and user interaction, and utilities for fetching and processing cryptocurrency data.

## Introduction

The primary goal of this project is to provide traders and analysts with a powerful set of tools to streamline their cryptocurrency trading and analysis workflows. The project leverages the Coinbase API to fetch real-time and historical data, and utilizes advanced natural language processing (NLP) techniques to enable users to interact with the system using natural language queries.

Key features of the project include:

- **Automated Trading Agent**: An intelligent agent capable of executing trades on the Coinbase exchange based on predefined strategies or user input.
- **Data Visualization**: A user-friendly web application that displays real-time and historical cryptocurrency data using interactive charts and visualizations.
- **Natural Language Processing**: Users can interact with the system using natural language queries, allowing them to retrieve information, execute trades, or perform analysis tasks.
- **Orderbook Analysis**: The system provides insights into the current orderbook for Bitcoin (BTC-USD) and identifies relevant trends for trading.
- **Historical Data Analysis**: Users can analyze historical cryptocurrency data, including candlestick charts and price movements.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository:

```
git clone https://github.com/username/crypto-trading-bot.git
```

2. Navigate to the project directory:

```
cd crypto-trading-bot
```

3. Install the required dependencies. It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using `venv` or `conda`.

```
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
pip install -r requirements.txt
```

4. Set up the required API keys and secrets. This project requires API keys for OpenAI (for natural language processing) and Tavily (for search functionality). You can obtain these keys from the respective service providers and add them to the Streamlit secrets file (`secrets.toml`) in the `.streamlit` directory.

```
# .streamlit/secrets.toml
OPENAI_API_KEY = "your_openai_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
```

## Usage

To run the main application, use the following command:

```
streamlit run app.py
```

This will launch the web application, where you can interact with the system, visualize data, and execute trades or analysis tasks.

To run the automated trading agent, use the following command:

```
python agent.py
```

This will start the agent, which will execute trades based on the predefined strategies or user input.

For more detailed usage instructions and examples, refer to the individual script files and their documentation.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

When contributing, please follow these guidelines:

1. Fork the repository and create a new branch for your contribution.
2. Make your changes and ensure that the tests pass.
3. Update the documentation if necessary.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need further assistance, please contact the project maintainers at [sbussiso321@gmail.com](mailto:sbussiso321@gmail.com).