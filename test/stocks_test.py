
# this is the "test/stocks_test.py" file...

from pandas import DataFrame

from app.stocks import fetch_stocks_csv


def test_data_fetching():

    stocks_df = fetch_stocks_csv("GOOGL")

    assert isinstance(stocks_df, DataFrame)

    assert "timestamp" in stocks_df.columns
    assert "adjusted_close" in stocks_df.columns

    assert len(stocks_df) >= 100

    # ideally we would test specific values
    # but this data gets refreshed every day
    # so that's why we're just kind of testing its structure (cols)
    # assert stocks_df["adjusted_close"][0] == 336.71
