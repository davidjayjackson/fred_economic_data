# Import Streamlit
import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas_datareader as pdr
# import plotly.express as px



# Title and Intro
st.title("Economic Indicators Dashboard")
st.write("Welcome to the economic indicators dashboard. Here you can explore data on unemployment, inflation, treasury rates, and mortgage rates.")

# Sidebar for filtering options
st.sidebar.title("Filters")
year_range = st.sidebar.slider("Select Year Range", min_value=1970, max_value=2023, value=(1990, 2020))

# Main Content
st.write(f"You have selected the year range: {year_range[0]} - {year_range[1]}")

# Placeholder for Plots (will be filled in subsequent steps)
st.write("Unemployment Rate Over Time")
unemployment_placeholder = st.empty()

st.write("Inflation Rate Over Time")
inflation_placeholder = st.empty()

st.write("30-Year Treasury Rates Over Time")
treasury_placeholder = st.empty()

st.write("30-Year Fixed Rate Mortgage Over Time")
mortgage_placeholder = st.empty()
