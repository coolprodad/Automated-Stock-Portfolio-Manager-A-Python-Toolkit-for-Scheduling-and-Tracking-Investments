#Importing the Required Libraries
import pandas as pd
import os

#Defining the Data handling Function
import pandas as pd
import os

def process_data(directory_path):
    # List to hold data from each file
    data_frames = []
    
    # Stock symbols you are interested in
    stock_symbols = ['MSFT', 'AAPL', 'NVDA', 'AMD', 'TSLA']
    
    # Process each stock file
    for symbol in stock_symbols:
        file_path = os.path.join(directory_path, f"{symbol}.csv")
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # You can add any specific processing here, for example:
            # df['Adjusted Close'] = df['Close'] * some_adjustment_factor
            
            # Append the DataFrame to our list
            data_frames.append(df)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {str(e)}")
    
    # Concatenate all dataframes into a single dataframe
    if data_frames:
        combined_df = pd.concat(data_frames, ignore_index=True)
        return combined_df
    else:
        return None

# Specify the path to your directory containing the CSV files
directory_path = '/Users/shashankkv/Desktop/Prototypes/Automation/Data'
processed_data = process_data(directory_path)

if processed_data is not None:
    print(processed_data.head())  # Print the first few rows of the combined data
else:
    print("No data to display.")
