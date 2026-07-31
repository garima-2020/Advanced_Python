import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data.csv')
 # print(df.head())
 # print(df.columns.tolist()) # Print the column names to understand the structure of the dataset

 # print(df.info())  # Print the summary of the dataset to understand the data types and missing values

 #  Data Cleaning and Preprocessing
# Drop rows with missing values in critical columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Strip whitespace from column names
print(df.columns.tolist())  # Print the cleaned column names to verify the changes
df = df.drop_duplicates()

# price to numeric

df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)  # Convert price to numeric
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)  # Convert area to numeric
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(float)  # Convert rate_per_sqft to numeric
print(df['price'])
print(df['area'])
print(df['rate_per_sqft'])