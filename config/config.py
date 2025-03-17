import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure Storage Configuration
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

# API Configuration
API_URL = os.getenv("API_URL")


