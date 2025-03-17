import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Azure Storage credentials from .env
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

def upload_to_blob(file_path, blob_name):
    """
    Upload a local file to Azure Blob Storage.
    """
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient(
            account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
            credential=STORAGE_ACCOUNT_KEY
        )

        # Get a BlobClient for the target file
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f" File '{blob_name}' successfully uploaded to Azure Blob Storage.")

    except Exception as e:
        print(f" Error uploading file: {e}")

if __name__ == "__main__":
    local_file = "data/products.parquet"  # Path of the file to upload
    blob_name = "products.parquet"  # Name of the file in Azure Blob Storage
    upload_to_blob(local_file, blob_name)
