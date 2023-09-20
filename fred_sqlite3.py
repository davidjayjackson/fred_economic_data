import pandas as pd
import sqlite3

unemployment= pd.read_excel('fred_data.xlsx',sheet_name="unemployment_data")
inflation= pd.read_excel('fred_data.xlsx',sheet_name="inflation_data")
treasury= pd.read_excel('fred_data.xlsx',sheet_name="treasury_data")
mortgage= pd.read_excel('fred_data.xlsx',sheet_name="mortgage_data")


# Create a connection to the database
conn = sqlite3.connect('unemployment_inflation_treasury_mortgage.sqlite3')

# Write the DataFrame to the database
unemployment.to_sql('unemployment', conn, if_exists='replace', index=False)
inflation.to_sql('inflation', conn, if_exists='replace', index=False)
treasury.to_sql('treasury', conn, if_exists='replace', index=False)
mortgage.to_sql('mortgage', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

