# Script: 019_upload_files_to_s3.py

import os
import boto3

def upload_files_to_s3(bucket_name, local_directory):
    """
    Uploads all files from a local directory to an S3 bucket.

    :param bucket_name: The name of the S3 bucket.
    :param local_directory: The local directory containing the files to upload.
    """
    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Walk through the local directory and upload each file
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, local_directory)  # Relate the file path to the directory

            try:
                # Upload the file to the specified S3 bucket
                s3.upload_file(file_path, bucket_name, s3_key)
                print(f"Uploaded {file_path} to {bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")

if __name__ == "__main__":
    # Example: Upload files from the './build' directory to the 'my-frontend-assets' bucket
    upload_files_to_s3("my-frontend-assets", "./build")
