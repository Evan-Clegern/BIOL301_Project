import pandas as pd
import matplotlib.pyplot as plt
import os

file_location = os.getcwd() + "\\COVID_data\\american_data_representative_wave.csv"

# Store the data into a DataFrame
american_data = pd.read_csv(file_location)
american_data = american_data.drop("Unnamed: 0",axis=1)

plt.plot(list(american_data.index),american_data["New_deaths"],".")
plt.xlabel("Days since Sep. 10th 2020")
plt.ylabel("New Deaths Recorded")
