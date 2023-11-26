from script import fetch_all_stock_data 
import matplotlib.pyplot as plt

#Ask the user to enter the stock symbol for the company they want data for.
#and return data for said company
def getSymbol():
   while True:
        stock_symbol = input("\nenter the stock symbol for the company (or 'exit' to quit):  ")

        if stock_symbol.lower() == 'exit':
            exit()

        # gets data from API
        data = fetch_all_stock_data(stock_symbol)

        # check for error
        if data.get('Error Message') is not None or 'Time Series (Daily)' not in data:
            print("please enter a viable symbol")
        else:
            return data
        
# Define a function that takes the time series number as an argument and returns the corresponding function name
def get_time_series_function():
    print("Enter the time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_series = input("Enter the number: ")

    time_series_dict = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }

    # Return the function name if the number is valid, otherwise return None
    return time_series_dict.get(time_series, None)

# Asks the user for the type of graph they want to see
def getGraphType():
    while True:
        print("Select graph type:")
        print("1. Line Graph")
        print("2. Bar Graph")
        
        graph_choice = input("Enter the number (or 'exit' to quit): ")
        if graph_choice.lower() == 'exit':
            exit()
            
        if graph_choice in ['1', '2']:
            return graph_choice
        else:
            print("Invalid selection. Please enter 1 for Line Graph or 2 for Bar Graph.")


# Function to visualize the stock data
def visualizeStockData(data, graph_type):
    time_series_data = data.get('Time Series (Daily)', {})
    dates = list(time_series_data.keys())[:10]  # Taking the latest 10 entries for better visualization
    closing_prices = [float(value['4. close']) for value in time_series_data.values()][:10]
    
    if graph_type == '1':  # Line Graph
        plt.plot(dates, closing_prices)
    elif graph_type == '2':  # Bar Graph
        plt.bar(dates, closing_prices)
    else:
        print("Invalid graph type.")
        return
    
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("Stock Data Visualization")
    plt.xticks(rotation=45)
    plt.show()

def main():
    print("Stock Data Visualizer")
    print("------------------------")
    stockData = getSymbol()

    if stockData:
        graphType = getGraphType()
        visualizeStockData(stockData, graphType)
        
    time_series = get_time_series_function()
    if time_series is not None:
        print(f"Selected time series function: {time_series}")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()