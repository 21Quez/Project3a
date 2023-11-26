import requests

# Function to make an API request to Alpha Vantage
def fetch_all_stock_data(symbol):
    api_key = '0X99GUZWNNPSOOQK'
    base_url = 'https://www.alphavantage.co/query'
    
    # Define the function to retrieve all data
    function = 'TIME_SERIES_DAILY'
    
    # Construct the API URL
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data from Alpha Vantage.")
        return None

if __name__ == "__main__":
    symbol = input("Enter the stock symbol: ")
    
    stock_data = fetch_all_stock_data(symbol)
    
    if stock_data:
        # Print the retrieved data
        print(stock_data)