import requests
import pandas as pd
import os

# Set the API endpoint URL
# This URL provides a list of products in JSON format
api_url = "https://dummyjson.com/products"

# Send a GET request to the API
# The response returns a dictionary with a key called "products"
response = requests.get(api_url)
data = response.json()

# Extract the list of products from the response
# Each product is a dictionary with different fields (id, title, price, etc.)
products = data["products"]

# Convert the list of products into a Pandas DataFrame
df = pd.DataFrame(products)

# Remove complex columns (like lists or dictionaries)
# These columns are not useful for simple analysis or saving to Parquet
for column in df.columns:
    if df[column].apply(lambda x: isinstance(x, (list, dict))).any():
        df.drop(columns=column, inplace=True)

# Drop text-heavy or irrelevant columns
for col in ["description", 
    "brand", 
    "warrantyInformation", 
    "shippingInformation", 
    "returnPolicy" , 
    "thumbnail", 
    "description", 
    "thumbnail", 
    "sku",
    "weight",
    "dimensions",
    "tags",
    "meta",
    "minimumOrderQuantity",
    "barcode",
    "images"]:
    if col in df.columns:
        df.drop(columns=col, inplace=True)      

# Determine the project root directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define output paths for both Parquet and CSV files
parquet_path = os.path.join(base_dir, "data", "raw", "products.parquet")
csv_path = os.path.join(base_dir, "data", "raw", "products.csv")

# Create the target directory if it does not already exist
os.makedirs(os.path.dirname(parquet_path), exist_ok=True)

df.to_parquet(parquet_path, index=False)
df.to_csv(csv_path, index=False, encoding="utf-8")

# Validation : Number of rows and columns, column names, and preview of the data
print(f"Data successfully saved to:\n- {parquet_path}\n- {csv_path}")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())