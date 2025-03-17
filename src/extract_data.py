import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL")

def fetch_data():
    """
    Fetch data from the DummyJSON API, remove non-primitive columns, and return a Pandas DataFrame.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()["products"]

        df = pd.DataFrame(data)

        # Identify all non-primitive columns by checking the entire dataframe
        non_primitive_columns = []
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                non_primitive_columns.append(col)

        # Remove non-primitive columns
        if non_primitive_columns:
            print(f" Removing non-primitive columns: {non_primitive_columns}")
            df = df.drop(columns=non_primitive_columns)

        return df

    except requests.exceptions.RequestException as e:
        print(f" Error fetching data: {e}")
        return None

def save_to_parquet(df, file_path="data/products.parquet"):
    """
    Save the cleaned DataFrame to a Parquet file.
    """
    if df is not None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_parquet(file_path, engine="pyarrow")
        print(f" Data successfully saved to {file_path}")
    else:
        print(" No data to save.")

if __name__ == "__main__":
    df = fetch_data()
    save_to_parquet(df)


