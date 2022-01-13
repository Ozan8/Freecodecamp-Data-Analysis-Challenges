import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x = df["Year"],
    y = df["CSIRO Adjusted Sea Level"])
    plt.xticks(range(1850,2076,25))
    

    # Create first line of best fit
    lin = linregress(x = df["Year"],
    y = df["CSIRO Adjusted Sea Level"])
    new_years = range(1880,2051,1)
    intercept = [lin.intercept + lin.slope * x for x in new_years]
    plt.plot(new_years,intercept, 'r' )
    


    # Create second line of best fit
    lin2 = linregress(x = df[df["Year"]>= 2000]["Year"], y = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])

    new_years2 = range(2000,2051,1)
    intercept2 = [lin2.intercept + lin2.slope * x for x in new_years2]
    plt.plot(new_years2,intercept2, 'r' )

    # Add labels and title
    plt.xlabel(xlabel = "Year")
    plt.ylabel(ylabel = 'Sea Level (inches)')
    plt.title(label = "Rise in Sea Level")
   
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()