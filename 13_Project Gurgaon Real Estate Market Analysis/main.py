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

# numerical columns cleaning

df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)  # Convert price to numeric
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)  # Convert area to numeric
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)  # Convert rate_per_sqft to numeric
print(df['price'])
print(df['area'])
print(df['rate_per_sqft'])

# Categorical columns cleaning
# df['location'] = df['location'].str.strip()  # Strip whitespace from location names

df['status'] = df['status'].str.strip().str.lower()  
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': 'True', 'not approved by rera': 'False'})  # Standardize RERA approval values
df['flat_type'] = df['flat_type'].str.strip().str.lower()  # Standardize flat type values

df = df.drop_duplicates()
print(df)
print(df.info())
# print(df['rera_approval'])


# Ouestion 1:Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
'''
lets write this output as a sentence:
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                     6.0
socity                              DLF Camellias
company_name                                  DLF
flat_type                               apartment
'''
print(f"The costliest flat in the dataset is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']}, built by {costliest_flat['builder_name']}. It is priced at {costliest_flat['price']} and has an area of {costliest_flat['area']} sqft with a rate of {costliest_flat['rate_per_sqft']} per sqft. The flat is currently {costliest_flat['status']} and has RERA approval status: {costliest_flat['rera_approval']}.") # another way to print the costliest flat details in a sentence format

# print(costliest_flat)

#Question 2: Which locality has the highest average price?
df.groupby('locality')['price'].mean().idxmax()
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")# f means format the string and print the locality with the highest average price

print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(20))  # Print the average price of each locality in descending order

# Question 3: Which locality has the highest rate per square foot?
highest_avg_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest average rate per square foot is {highest_avg_rate_locality}.")  

# Question 4: Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print(f"Yes, ready-to-move properties cost more on average ({ready_to_move_avg_price}) than under-construction properties ({under_construction_avg_price}).")

# Question 5: Do RERA-approved properties command a price premium?    
rera_approved_avg_price = df[df['rera_approval'] == 'True']['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == 'False']['price'].mean()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print(f"Yes, RERA-approved properties command a price premium on average ({rera_approved_avg_price}) compared to non-RERA-approved properties ({not_rera_approved_avg_price}).")

# Question 6: How does area (sqft) impact property price?
area_price_correlation = df['area'].corr(df['price'])
print(f"The correlation between area and price is {area_price_correlation}.")

# Question 7: Which BHK configuration is the most expensive on average?
bhk_avg_prices = df.groupby('bhk_count')['price'].mean()
most_expensive_bhk = bhk_avg_prices.idxmax()
print(f"The {most_expensive_bhk}-BHK configuration is the most expensive on average.")

# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_prices = df.groupby('property_type')['price'].mean()
costliest_property_type = property_type_avg_prices.idxmax() 
print(f"The {costliest_property_type} property type is the costliest on average.")

# Question 9: Do certain builders or companies consistently price higher?
builder_avg_prices = df.groupby('builder_name')['price'].mean()
print(builder_avg_prices.sort_values(ascending=False).head(10))  # Print the average price of each builder in descending order

# Question 10: Are larger homes always more expensive per square foot?
area_rate_correlation = df['area'].corr(df['rate_per_sqft'])    
print(f"The correlation between area and rate per square foot is {area_rate_correlation}.")