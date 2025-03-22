# Script: 007_upload_to_gcs.py

from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the GCS bucket.
        source_file_name (str): The path to the local file to upload.
        destination_blob_name (str): The name of the destination object in GCS.
    """
    try:
        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Create a blob object for the destination
        blob = bucket.blob(destination_blob_name)
        
        # Upload the file to GCS
        blob.upload_from_filename(source_file_name)
        
        # Confirm the upload
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        # Handle exceptions
        print(f"Error uploading file to GCS: {e}")

# Example usage
if __name__ == '__main__':
    upload_blob('your-bucket-name', 'local-file-to-upload.txt', 'destination-object-name')
