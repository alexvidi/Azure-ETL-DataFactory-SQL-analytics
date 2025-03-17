import os
import pandas as pd
import pyodbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database credentials from .env
SERVER = os.getenv("SQL_SERVER")
DATABASE = os.getenv("SQL_DATABASE")
USERNAME = os.getenv("SQL_USERNAME")
PASSWORD = os.getenv("SQL_PASSWORD")

# Connection string
conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

def load_data_to_sql(file_path):
    """
    Load Parquet data from a local file into Azure SQL Database.
    """
    try:
        # Read Parquet file
        df = pd.read_parquet(file_path)

        # Connect to Azure SQL Database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Insert data into SQL table
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO products (id, title, description, price, brand, category, rating)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, row["id"], row["title"], row["description"], row["price"], row["brand"], row["category"], row["rating"])

        # Commit and close connection
        conn.commit()
        cursor.close()
        conn.close()

        print(f" Data successfully loaded into {DATABASE}.products")

    except Exception as e:
        print(f" Error loading data into SQL: {e}")

if __name__ == "__main__":
    load_data_to_sql("data/products.parquet")
