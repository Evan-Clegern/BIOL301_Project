import pandas as pd
import os

file_location = os.getcwd() + "\\COVID_data\\raw_data.csv"

# Store the data into a DataFrame
preprocessed_data = pd.read_csv(file_location)

# Replace NaN new_cases or new_deaths with 0s
preprocessed_data = preprocessed_data.fillna(0)

# Get data from the U.S. only (for simplicity and speed)
american_data = preprocessed_data[preprocessed_data["Country"]=="United States of America"]

# Get only the data we care about
american_data = american_data.drop(["Country_code","WHO_region","Cumulative_cases","Cumulative_deaths"],axis=1)

# Reset the indices of the rows
american_data = american_data.reset_index()
american_data = american_data.drop("index",axis=1)

# Narrow down the selection
american_data = american_data.head(425)
american_data = american_data.tail(175)

american_data.to_csv(os.getcwd() + "\\COVID_data\\american_data_representative_wave.csv", ",", "0")
