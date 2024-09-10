import yfinance as yf
import pandas as pd
import os
import schedule
import time

# Define stock symbols and other parameters
stocks = ['MSFT', 'AAPL', 'TSLA', 'NVDA', 'AMD']
historical_interval = '1d'  # For the past 6 months, use daily data
update_interval = '1h'      # For scheduled updates, use 1-hour interval (6h not supported for long periods)
period = '6mo'              # Last 6 months (initial data)

# Define the local directory to save the stock data
local_dir = '/Users/shashankkv/Desktop/Prototypes/Automation/Data'  # Your specified directory

# Ensure the directory exists
os.makedirs(local_dir, exist_ok=True)

# Function to download and save or update stock data
def download_and_update_stock_data():
    for stock in stocks:
        # Download stock data for the last 6 months using daily data
        data = yf.download(stock, period=period, interval=historical_interval)
        
        # Define the CSV file path
        file_path = os.path.join(local_dir, f"{stock}.csv")
        
        # Check if the CSV file already exists
        if os.path.exists(file_path):
            # If it exists, read the existing data
            existing_data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
            
            # Concatenate the existing data with the new data, dropping any duplicates
            combined_data = pd.concat([existing_data, data]).drop_duplicates()
            
            # Save the updated data to the same CSV file
            combined_data.to_csv(file_path)
            print(f"Data for {stock} updated and saved to {file_path}")
        else:
            # If the file doesn't exist, create it with the downloaded data
            data.to_csv(file_path)
            print(f"Data for {stock} saved to {file_path}")

# Function to update stock data every 6 hours using 1-hour interval for the last 6 hours
def update_stock_data_every_6_hours():
    for stock in stocks:
        # Download stock data for the last 7 days using 1-hour interval (since 6h isn't supported)
        data = yf.download(stock, period='7d', interval=update_interval)
        
        # Define the CSV file path
        file_path = os.path.join(local_dir, f"{stock}.csv")
        
        # If the CSV file already exists, append the new data to the file
        if os.path.exists(file_path):
            existing_data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
            combined_data = pd.concat([existing_data, data]).drop_duplicates()
            combined_data.to_csv(file_path)
            print(f"Data for {stock} updated and saved to {file_path}")
        else:
            data.to_csv(file_path)
            print(f"Data for {stock} saved to {file_path}")

# Step 1: Run immediately to download the last 6 months' data (daily interval)
print("Starting immediate stock data extraction for the past 6 months (daily data)...")
download_and_update_stock_data()

# Step 2: Schedule the job to update the data every 6 hours
print("Scheduling stock data extraction every 6 hours (1-hour interval)...")
schedule.every(6).hours.do(update_stock_data_every_6_hours)

# Run the job continuously
while True:
    schedule.run_pending()
    time.sleep(1)
