# Script: 008_upload_to_azure_blob.py

import os
from azure.storage.blob import BlobServiceClient

try:
    # Get Azure Storage connection string from environment
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    
    if not connect_str:
        raise ValueError("Azure Storage connection string not found in environment variables.")
    
    # Create the BlobServiceClient object
    blob_client = BlobServiceClient.from_connection_string(connect_str).get_blob_client(
        container='your-container-name', 
        blob='your-blob-name'
    )
    
    # Upload data to the blob
    with open("local-file-to-upload.txt", "rb") as data:
        blob_client.upload_blob(data, overwrite=True)  # Added overwrite=True to avoid conflict
    
    # Confirm the upload
    print("File uploaded to Azure Blob Storage")
except Exception as e:
    # Handle exceptions
    print(f"An error occurred: {e}")
