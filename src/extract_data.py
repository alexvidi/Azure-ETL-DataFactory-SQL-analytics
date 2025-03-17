import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API URL from environment variables
API_URL = os.getenv("API_URL")

def fetch_data():
    """
    Fetch data from the DummyJSON API and return as a Pandas DataFrame.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()["products"]
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f" Error fetching data: {e}")
        return None

def save_to_parquet(df, file_path="data/products.parquet"):
    """
    Save the DataFrame to a Parquet file.
    """
    if df is not None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        df.to_parquet(file_path, engine="pyarrow")
        print(f" Data successfully saved to {file_path}")
    else:
        print(" No data to save.")

if __name__ == "__main__":
    df = fetch_data()
    save_to_parquet(df)
