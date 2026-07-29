import pandas as pd 

data = {
    "name" : ["Ali" , "Sara" , "John"],
    "marks" : [80,89,78]
}

df = pd.DataFrame(data)
print(df)

# Functions 
print(df.head()) # top 5 rows
print(df.tail()) # last 5 rows
print(df.info())
print(df.describe()) # gives all count min max all

print(df["marks"]) # selecting the marks col only
print(df[["name", "marks"]]) # selecting two columns