import pandas as pd

df = pd.DataFrame({
    "Product Name": ["iPhone 14", "Samsung Galaxy", "OnePlus 11", "Pixel 7", None] * 200,
    "price": ["499", "799", "1199", "899", None] * 200,
    "category": ["Mobile", "mobile", "ELECTRONICS", "Electronics", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes", "no", None] * 200,
    "launch year": ["2023", "2022", "2021", "2020", None] * 200
})

print(df)
print(df["price"]) # single rows
print(df[["price", "category", "rating"]]) # multipl erows


# Selecting Rows with Conditions

# Filter rows using conditions:

print(df[df["price"] > "500"]) # df["price"] contains strings like "499", "799", "1,199".
# 500 is an integer.
# Python cannot compare a string with an integer.

# Multiple conditions:

print(df[(df["price"] > "500") & (df["rating"] >= 4)])

# missing values
print(df.isna()) # jha pr bhi null hoga vha pr true aajayega

print(df.isna().sum()) # sum krke btayega ki kis col me kitte null h 

print(df.dropna()) # wo rows jha pr na nii h 

# filling the missing column
df["rating"] = df["rating"].fillna(df["rating"].mean())
print(df)

# renaming col
df = df.rename(columns={"Product Name": "product_name"})

# changing datatype
print(df.dtypes)

# convert types
df["price"] = df["price"].astype(float)
print(df.dtypes)

# removing duplicates
df.drop_duplicates()

# cleaning 
df["category"] = df["category"].str.lower().str.strip()