# Script: 024_download_from_azure_blob.py

from azure.storage.blob import BlobServiceClient

# Initialize the Blob Service Client
connection_string = "your-azure-storage-connection-string"  # Replace with your connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Parameters for Blob
container_name = "your-container-name"  # Replace with your container name
blob_name = "your-blob-name"  # Replace with your blob name
download_file_path = "path/to/downloaded/file"  # Replace with the path where the file should be downloaded

try:
    # Initialize the Blob Client for the specific blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download the blob
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    print(f"Blob {blob_name} downloaded to {download_file_path}.")
except Exception as e:
    print(f"An error occurred during the download: {e}")
