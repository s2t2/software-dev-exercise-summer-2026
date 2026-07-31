
import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px
import matplotlib.pyplot as plt

load_dotenv() # loads environment variables from the ".env" file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def format_usd(price):
    return f"${price:.2f}"


def fetch_stocks_csv(symbol="NFLX"):
    """Fetches stock data from the AlphaVantage API.

    Params:
        symbol (str) like "NFLX"

    Return a pandas DataFrame with the time series data.
    """
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    stocks_df = read_csv(request_url)
    return stocks_df


if __name__ == "__main__":

    # FETCH THE DATA

    symbol = input("Please choose a stock symbol: ") or "NFLX"

    stocks_df = fetch_stocks_csv(symbol)
    print(stocks_df.head())

    # CHART THE DATA

    fig = px.line(stocks_df, x="timestamp", y="adjusted_close",
                title=f"Stock Prices ({symbol})",
                height=450
                )
    fig.show()

    # alternatively, if plotly is acting up...

    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.plot(stocks_df["timestamp"], stocks_df["adjusted_close"])

    ax.set_title(f"Stock Prices ({symbol})")
    ax.set_xlabel("timestamp")
    ax.set_ylabel("adjusted_close")

    plt.tight_layout()
    plt.show()
