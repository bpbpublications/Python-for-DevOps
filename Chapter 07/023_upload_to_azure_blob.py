# Script: 023_upload_to_azure_blob.py

from azure.storage.blob import BlobServiceClient

# Initialize the Blob Service Client
connection_string = "your-azure-storage-connection-string"  # Replace with your connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Parameters for Blob
container_name = "your-container-name"  # Replace with your container name
blob_name = "your-blob-name"  # Replace with your blob name
file_path = "path/to/your/local/file"  # Replace with the path to your local file

try:
    # Create a blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Upload the blob
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)  # Added overwrite=True to avoid conflicts

    print(f"Blob {blob_name} uploaded to container {container_name}.")
except Exception as e:
    print(f"An error occurred during the upload: {e}")
