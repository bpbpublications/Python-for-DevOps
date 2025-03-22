# Script: 018_create_s3_bucket.py

import boto3

def create_s3_bucket(bucket_name, region="us-east-1"):
    """
    Creates an S3 bucket in the specified region.

    :param bucket_name: The name of the S3 bucket to be created.
    :param region: The AWS region where the bucket will be created (default is "us-east-1").
    """
    # Initialize the S3 client
    s3 = boto3.client('s3', region_name=region)

    try:
        # Create the S3 bucket with the specified name and region
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}  # Set the region for the bucket
        )
        print(f"Bucket {bucket_name} created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

if __name__ == "__main__":
    # Example: Create an S3 bucket named 'my-frontend-assets' in the default region
    create_s3_bucket("my-frontend-assets")
