import requests
import sys

# Replace 'YOUR_API_KEY' with your actual API key from Polygon.io
API_KEY = 'ZGLituVvaZgEpEX91dF9GpbsDdgXxawN'

# Define the base URL for Polygon.io API
BASE_URL = 'https://api.polygon.io'

def get_aggregate_bars(ticker, multiplier, timespan, from_date, to_date, adjusted=True, sort='asc', limit=120):
    url = f'{BASE_URL}/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}'

    params = {
        'adjusted': adjusted,
        'sort': sort,
        'limit': limit,
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_grouped_daily(locale, date, adjusted=True, include_otc=False):
    url = f'{BASE_URL}/aggs/grouped/locale/{locale}/market/stocks/{date}'

    params = {
        'adjusted': adjusted,
        'include_otc': include_otc,
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_daily_open_close(ticker, date, adjusted=True):
    url = f'{BASE_URL}/v1/open-close/{ticker}/{date}'

    params = {
        'adjusted': adjusted,
        'apiKey': API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
    except ValueError as e:
        print("JSON Decode Error:", e)

    return None  # Return None if there's an error

def get_previous_close(ticker, adjusted=True):
    url = f'{BASE_URL}/aggs/ticker/{ticker}/prev'

    params = {
        'adjusted': adjusted,
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_trades(stock_ticker, timestamp=None, order=None, limit=10, sort=None):
    url = f'{BASE_URL}/v2/aggs/ticker/{ticker}/prev'

    params = {
        'apiKey': API_KEY,
        'timestamp': timestamp,
        'order': order,
        'limit': limit,
        'sort': sort
    }

    response = requests.get(url, params=params)
    print(response.json())

if __name__ == "__main__":
    ticker = 'AAPL'
    date = '2023-01-09'

    # Get daily open/close data
    daily_open_close_data = get_daily_open_close(ticker, date)
    print("\nDaily Open/Close Data:")
    print(daily_open_close_data)

    # Get trades data
    stock_ticker = 'AAPL'
    trades_data = get_trades(stock_ticker)
    print("\nTrades Data:")
    print(trades_data)

    sys.exit()  # Exit the code when done running
