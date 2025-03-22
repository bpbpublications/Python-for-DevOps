# Script: 020_gcp_storage_download.py

from google.cloud import storage
from google.api_core.exceptions import GoogleAPICallError, Forbidden

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """
    Downloads a blob from the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the GCS bucket.
        source_blob_name (str): The name of the blob in GCS.
        destination_file_name (str): The path where the file will be downloaded locally.
    """
    try:
        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        
        # Retrieve the bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Get the blob object
        blob = bucket.blob(source_blob_name)
        
        # Download the blob
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
    except Forbidden:
        print("Error: Permission denied. Ensure you have access to the bucket and blob.")
    except GoogleAPICallError as e:
        print(f"Google API error occurred: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    download_blob('your-bucket-name', 'storage-object-name.txt', 'path/to/local/file.txt')
