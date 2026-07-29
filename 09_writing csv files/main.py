import pandas as pd


# Create a sample DataFrame of Ecommerce order data
df = pd.DataFrame({
    'Order ID': [1001, 1002, 1003, 1004],
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Quantity': [1, 2, 1, 3],
    'Price': [1200.00, 800.00, 300.00, 150.00]
})

# save the DataFrame to a CSV file
df.to_csv('ecommerce_orders.csv', index=False)