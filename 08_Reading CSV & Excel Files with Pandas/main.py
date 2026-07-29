import pandas as pd

df = pd.read_csv("data.csv")
print(df)

 #Common CSV Issues
# Custom Separator
pd.read_csv("data.csv", sep=";")

# Skipping Rows
pd.read_csv("data.csv", skiprows=2)

#Selecting Specific Columns
pd.read_csv("data.csv", usecols=["name", "price"])


# Reading Excel Files

# Excel files often contain multiple sheets.

df = pd.read_excel("data.xlsx")

# Read a specific sheet:

pd.read_excel("data.xlsx", sheet_name="Sheet1")

# List all sheet names:

pd.ExcelFile("data.xlsx").sheet_names