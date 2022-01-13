import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv")
df = df.set_index("date")
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df["value"] <= df["value"].quantile(.975)) & (df["value"] >= df["value"].quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plt.plot(df.index,df["value"])
    plt.plot(df.index,df["value"])
    plt.ylabel("Page Views")
    plt.xlabel("Date")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    caterog = df_bar.groupby([df.index.year, df.index.month,])["value"].agg(np.mean).rename_axis(["year","month"])
    caterog = caterog.reset_index()
    
    
    
    # Draw bar plot
    
     
    df_pivot = pd.pivot_table(caterog, values="value", index="year", columns= "month")
    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(3,4)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend( ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",])
    



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    
    
    # Draw box plots (using Seaborn)
    fig,(ax1,ax2) = plt.subplots(1,2)
    #fig.set_size_inches(3,3)

    ax1 = sns.boxplot(x = df_box['year'], y = df_box["value"], ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title("Year-wise Box Plot (Trend)")

    ax2 = sns.boxplot(x =df_box["month"], y=df_box["value"], ax=ax2 , order=['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    df_box["value"].head()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    