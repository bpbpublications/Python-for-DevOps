# Script: 023_upload_react_app_to_s3.py

import boto3
import os

def upload_to_s3(bucket_name, local_directory):
    """
    Uploads all files from a local directory to an S3 bucket.

    :param bucket_name: The name of the S3 bucket to upload files to.
    :param local_directory: The local directory containing the files to upload.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Walk through the local directory and upload each file to S3
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, local_directory)  # Relate the file path to the directory

            try:
                # Upload the file to the specified S3 bucket
                s3_client.upload_file(file_path, bucket_name, s3_key)
                print(f"Uploaded {file_path} to {bucket_name}/{s3_key}")
            except Exception as e:
                # Catch and print errors during file upload
                print(f"Error uploading {file_path}: {e}")

if __name__ == "__main__":
    # Example: Upload the built React app files from the './my-react-app/build' directory
    upload_to_s3("my-react-app-bucket", "./my-react-app/build")
