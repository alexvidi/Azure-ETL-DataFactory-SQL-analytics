import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Step 1: Load environment variables from the .env file
# The .env file contains sensitive configuration like Azure Storage account name, key, and container name
# These values are stored outside the script for better security and flexibility
load_dotenv()

# Step 2: Read the values from the environment
# These variables connect to Azure Blob Storage account
storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")   # Azure Storage account name
storage_account_key = os.getenv("STORAGE_ACCOUNT_KEY")     # The access key for account
container_name = os.getenv("CONTAINER_NAME")               # The name of the blob container created in Azure

# Step 3: Define the local file path and the name it will have in the Azure container
# File upload to the cloud
local_file_path = "data/raw/products.parquet"              # Path to the file on local machine
blob_name = "products.parquet"                             # Name to give the file in Azure Blob Storage

# Step 4: Create a client that connects to Azure Storage account
# BlobServiceClient is the object that allows to manage and access blobs (files) in Azure
blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account_name}.blob.core.windows.net",
    credential=storage_account_key
)

# Step 5: Create a client for the file (blob) to upload
# Client will be used to send the file to the correct container and location
blob_client = blob_service_client.get_blob_client(
    container=container_name,
    blob=blob_name
)

# Step 6: Open the local file and upload it to Azure Blob Storage
# The file is opened in binary mode ("rb") so it can be read correctly
# The parameter overwrite=True means that if the file already exists, it will be replaced
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

# Step 7: Print a confirmation message
# This message confirms that the upload was completed successfully
print(f"File '{blob_name}' successfully uploaded to Azure Blob Storage in container '{container_name}'.")