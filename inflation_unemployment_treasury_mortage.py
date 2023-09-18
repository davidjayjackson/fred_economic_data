import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as pdr
import plotly.express as px
# --------------------------------------------------------------------------------------------------------------------------
# Unemployment Rate Over Time
# View data of the unemployment rate, or the number of people 16 and over actively searching for a job as a percentage of the total labor force.

unemployment_data = pdr.get_data_fred('UNRATE')
fig = px.line(unemployment_data, x=unemployment_data.index, y='UNRATE', title='Unemployment Rate Over Time')
fig.update_xaxes(rangeslider_visible=True)
fig.show()

# Unemployment Rate Over Time (Year over Year)

# Extracting month and year from the index
unemployment_data['Month'] = unemployment_data.index.month
unemployment_data['Year'] = unemployment_data.index.year

# Resetting index for plotting
unemployment_data_reset = unemployment_data.reset_index(drop=True)

# Creating the plot
fig = px.line(unemployment_data_reset, x='Month', y='UNRATE', color='Year', title='Unemployment Rate Over Time (Yr over Yr)')

# Updating x-axis to show only months
fig.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig.show()

# Unemployment Rate Excluding 2020
# Filtering the data to exclude the year 2020
unemployment_data_exclude_2020 = unemployment_data_reset[unemployment_data_reset['Year'] != 2020]

# Creating the plot excluding 2020 data
fig_exclude_2020 = px.line(unemployment_data_exclude_2020, x='Month', y='UNRATE', color='Year', title='Unemployment Rate Excluding 2020')

# Updating x-axis to show only months
fig_exclude_2020.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig_exclude_2020.show()

# ------------------------------------------------------------------------------------------------------------------------------
# Inflation Rate Data (Consumer Price Index: CPI), Index 1982-1984=100, Monthly, Not Seasonally AdjustedJan 1913 to Aug 2023 (4 days ago). 
# View data of the CPI, or an inflation measure derived from tracking the changes in the weighted-average **price of a basket** of common goods and services.

# Retrieving inflation rate data (Consumer Price Index)
inflation_data = pdr.get_data_fred('CPIAUCNS')
inflation_data.describe()
# Creating a single line plot for inflation rate data with dates on the x-axis
fig_single_line = px.line(inflation_data, x=inflation_data.index, y='CPIAUCNS', title='Inflation Rate Over Time')

# Adding a date slider to the plot
fig_single_line.update_xaxes(rangeslider_visible=True)

fig_single_line.show()

# Inflation Rate by Month and Year
# Extracting month and year from the index for inflation data
inflation_data['Month'] = inflation_data.index.month
inflation_data['Year'] = inflation_data.index.year

# Resetting index for plotting
inflation_data_reset = inflation_data.reset_index(drop=True)

# Creating the plot with the same settings as the unemployment rate plot
fig_inflation = px.line(inflation_data_reset, x='Month', y='CPIAUCNS', color='Year', title='Inflation Rate by Month and Year')

# Updating x-axis to show only months
fig_inflation.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig_inflation.show()

# Inflation Rate Over Time (in %)

# Calculating the inflation rate in percentage
inflation_data['Inflation_Rate'] = inflation_data['CPIAUCNS'].pct_change() * 100  # pct_change computes percentage change

# Filtering out the first row since percentage change from the first to the second row will result in a NaN value
inflation_data_filtered = inflation_data.dropna()

# Creating a single line plot for inflation rate in percentage with dates on the x-axis
fig_inflation_percent = px.line(inflation_data_filtered, x=inflation_data_filtered.index, y='Inflation_Rate', title='Inflation Rate Over Time (in %)')

# Adding a date slider to the plot
fig_inflation_percent.update_xaxes(rangeslider_visible=True)

fig_inflation_percent.show()

# Year-Over-Year Inflation Rate (in %)

# Calculating the year-over-year inflation rate in percentage
inflation_data['YoY_Inflation_Rate'] = inflation_data['CPIAUCNS'].pct_change(periods=12) * 100  # Using periods=12 for year-over-year change

# Filtering out the rows with NaN values (the first 12 rows will have NaN values for YoY inflation rate)
inflation_data_filtered_yoy = inflation_data.dropna(subset=['YoY_Inflation_Rate'])

# Creating a single line plot for year-over-year inflation rate in percentage with dates on the x-axis
fig_inflation_yoy = px.line(inflation_data_filtered_yoy, x=inflation_data_filtered_yoy.index, y='YoY_Inflation_Rate', title='Year-Over-Year Inflation Rate (in %)')

# Adding a date slider to the plot
fig_inflation_yoy.update_xaxes(rangeslider_visible=True)

fig_inflation_yoy.show()

# ---------------------------------------------------------------------------------------------------------------------------------
### 30 year treasury rates
# Percent, Monthly, Not Seasonally AdjustedFeb 1977 to Aug 2023 (Sep 1)
# Yields on actively traded non-inflation-indexed issues adjusted to constant maturities. The 30-year Treasury constant maturity series was discontinued on February 18, 2002, and reintroduced on February 9, 2006.
#### 30-Year Treasury Rates Over Time

# Retrieving 30-year treasury rates data
treasury_data = pdr.get_data_fred('GS30')

# Extracting month and year from the index for treasury data
treasury_data['Month'] = treasury_data.index.month
treasury_data['Year'] = treasury_data.index.year

# Resetting index for plotting
treasury_data_reset = treasury_data.reset_index(drop=True)

# Creating a single line plot for 30-year treasury rates with dates on the x-axis
fig_treasury_single_line = px.line(treasury_data, x=treasury_data.index, y='GS30', title='30-Year Treasury Rates Over Time')

# Adding a date slider to the plot
fig_treasury_single_line.update_xaxes(rangeslider_visible=True)

fig_treasury_single_line.show()

# 30-Year Treasury Rates by Year

# Resetting index for plotting
treasury_data_reset = treasury_data.reset_index(drop=True)

# Creating the plot for 30-year treasury rates with one line for each year
fig_treasury_by_year = px.line(treasury_data_reset, x='Month', y='GS30', color='Year', title='30-Year Treasury Rates by Year')

# Updating x-axis to show only months
fig_treasury_by_year.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig_treasury_by_year.show()

# -------------------------------------------------------------------------------------------------------------------------
# 30-Year Fixed Rate Mortgage Average

unemployment_data = pdr.get_data_fred('MORTGAGE30US')
fig = px.line(unemployment_data, x=unemployment_data.index, y='MORTGAGE30US', title='30-Year Fixed Rate Mortgage Average')
fig.update_xaxes(rangeslider_visible=True)
fig.show()

# 30-Year Fixed Rate Mortgage  (Year over Year)

 Extracting month and year from the index
unemployment_data['Month'] = unemployment_data.index.month
unemployment_data['Year'] = unemployment_data.index.year

# Resetting index for plotting
unemployment_data_reset = unemployment_data.reset_index(drop=True)

# Creating the plot
fig = px.line(unemployment_data_reset, x='Month', y='MORTGAGE30US', color='Year', title='30-Year Fixed Rate Mortgage Over (Yr over Yr)')

# Updating x-axis to show only months
fig.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig.show()

# 30 Year Mortage Rate Excluding 2020

# Filtering the data to exclude the year 2020
unemployment_data_exclude_2020 = unemployment_data_reset[unemployment_data_reset['Year'] != 2020]

# Creating the plot excluding 2020 data
fig_exclude_2020 = px.line(unemployment_data_exclude_2020, x='Month', y='MORTGAGE30US', color='Year', title='30-Year Fixed Rate Mortgage Excluding 2020')

# Updating x-axis to show only months
fig_exclude_2020.update_xaxes(
    tickmode='array',
    tickvals=list(range(1, 13)),
    ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
)

fig_exclude_2020.show()