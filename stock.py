# Import libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define a function that takes the time series number as an argument and returns the corresponding function name
def get_time_series_function(time_series):
    # Use a dictionary to map the numbers to the function names
    time_series_dict = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }
    # Return the function name if the number is valid, otherwise return None
    return time_series_dict.get(time_series, None)

# Define a function that takes the symbol, chart type, time series, start date and end date as arguments and plots the data
def plot_stock_data(symbol, chart_type, time_series, start_date, end_date):
    # Get the API key from Alpha Vantage
    api_key = "0X99GUZWNNPSOOQK"
    # Build the API URL
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": get_time_series_function(time_series),
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "full",
        "datatype": "json"
    }
    # Send HTTP request and get response
    response = requests.get(base_url, params=params)
    data = response.json()
    # Parse JSON data and convert to DataFrame
    if "Error Message" in data:
        print("Invalid symbol or function. Please try again.")
        return
    else:
        # Get the key for the time series data
        ts_key = list(data.keys())[1]
        # Get the nested dictionary of time series data
        ts_data = data[ts_key]
        # Convert the dictionary to a DataFrame
        df = pd.DataFrame.from_dict(ts_data, orient="index")
        # Rename the columns
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        # Convert the index to datetime format
        df.index = pd.to_datetime(df.index)
        # Sort the DataFrame by date
        df = df.sort_index()
        # Filter the DataFrame by date range
        df = df.loc[start_date:end_date]
    # Plot the data according to chart type
    if chart_type == "line":
        # Use matplotlib.pyplot to create line charts for open, close, high, and low prices
        plt.plot(df.index, df["Open"], label="Open")
        plt.plot(df.index, df["Close"], label="Close")
        plt.plot(df.index, df["High"], label="High")
        plt.plot(df.index, df["Low"], label="Low")
    elif chart_type == "bar":
        # Use matplotlib.pyplot to create a bar chart of close prices
        plt.bar(df.index, df["Open"], label="Open")
        plt.bar(df.index, df["Close"], label="Close")
        plt.bar(df.index, df["High"], label="High")
        plt.bar(df.index, df["Low"], label="Low")

    plt.title(f"{symbol} Prices from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()  # Add a legend to distinguish open, close, high, and low lines
    plt.show()

# Define a main function that asks for user input and calls the plot_stock_data function
def main():
    # Ask user for input
    print("Stock Data Visualizer")
    print("------------------------")
    symbol = input("Enter the stock symbol: ")
    chart_type = input("Enter the chart type (line or bar): ")
    # Ask user for the time series function with a list of options and a number
    print("Enter the time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_series = input("Enter the number: ")
    
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Validate user input for date range and chart type
    if end_date < start_date:
        print("Invalid date range. Please try again.")
        return
    if chart_type not in ["line", "bar"]:
        print("Invalid chart type. Please try again.")
        return

    # Call the plot_stock_data function with user input as arguments
    plot_stock_data(symbol, chart_type, time_series, start_date, end_date)

# Call the main function
if __name__ == "__main__":
    main()

answer = input("Would you like to look at another stock (Y/n)")
mod_answer = answer.lower()
if mod_answer == "y":
    main()