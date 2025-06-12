import requests
import pandas as pd
import os

# Step 1: Set the API endpoint URL
# This URL provides a list of products in JSON format
api_url = "https://dummyjson.com/products"

# Step 2: Send a GET request to the API
# The response returns a dictionary with a key called "products"
response = requests.get(api_url)
data = response.json()

# Step 3: Extract the list of products from the response
# Each product is a dictionary with different fields (id, title, price, etc.)
products = data["products"]

# Step 4: Convert the list of products into a Pandas DataFrame
# A DataFrame is like a table where each row is a product and each column is a field
df = pd.DataFrame(products)

# Step 5: Remove complex columns (like lists or dictionaries)
# These columns are not useful for simple analysis or saving to Parquet
for column in df.columns:
    if df[column].apply(lambda x: isinstance(x, (list, dict))).any():
        df.drop(columns=column, inplace=True)

# Step 6: Create the output folder
# This ensures that the folder 'data/raw' is available to save the file
os.makedirs("data/raw", exist_ok=True)

# Step 7: Save the cleaned DataFrame to a Parquet file
# Parquet is a modern file format that is fast and efficient for large datasets
output_path = "data/raw/products.parquet"
df.to_parquet(output_path, index=False)

# Confirm success
print(f"Data successfully saved to {output_path}")

# Validation
print("Shape:", df.shape)  # Number of rows and columns
print("Columns:", df.columns.tolist())  # List of column names
print(df.head())  # Preview of the first 5 rows