import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  data = pd.read_csv("epa-sea-level.csv")
  
    # Create scatter plot
  plt.figure(figsize=(10, 6))
plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], label="Actual Data")

    # Create lines for prediction
plt.plot([1880, 2050], [data["CSIRO Adjusted Sea Level"].iloc[0], data["CSIRO Adjusted Sea Level"].iloc[-1]], color='red', label="Prediction (1880-2050)")
plt.plot([2000, 2050], [data[data["Year"] == 2000]["CSIRO Adjusted Sea Level"].values[0], data["CSIRO Adjusted Sea Level"].iloc[-1]], color='green', label="Prediction (2000-2050)")


    # Add labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()
    
# Save plot and return data for testing (DO NOT MODIFY)
plt.savefig('sea_level_plot.png')