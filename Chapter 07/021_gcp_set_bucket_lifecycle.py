# Script: 021_gcp_set_bucket_lifecycle.py

from google.cloud import storage
from google.api_core.exceptions import GoogleAPICallError, Forbidden

def set_bucket_lifecycle(bucket_name):
    """
    Sets the lifecycle policy for a Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the GCS bucket.
    """
    try:
        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        
        # Retrieve the bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Define the lifecycle rule
        bucket.add_lifecycle_delete_rule(age=365)  # Delete objects older than 365 days
        
        # Apply the lifecycle rule
        bucket.patch()
        print(f"Lifecycle rules set for bucket {bucket_name}.")
    except Forbidden:
        print("Error: Permission denied. Ensure you have access to modify the bucket.")
    except GoogleAPICallError as e:
        print(f"Google API error occurred: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    set_bucket_lifecycle('your-bucket-name')
