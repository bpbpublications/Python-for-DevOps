# Script: 017_create_rds_snapshot.py

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Initialize a Boto3 client for RDS
rds_client = boto3.client('rds')

# RDS instance and snapshot identifiers
db_instance_id = 'mydbinstance'
snapshot_id = 'mydbinstance-snapshot'

try:
    # Create a snapshot of an RDS instance
    response = rds_client.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier=db_instance_id
    )
    # Print response for confirmation
    print("RDS snapshot creation initiated:", response)

except NoCredentialsError:
    # Handle missing AWS credentials
    print("Error: AWS credentials not found. Please configure your credentials.")
except PartialCredentialsError:
    # Handle incomplete AWS credentials
    print("Error: Incomplete AWS credentials provided. Please check your credentials.")
except ClientError as e:
    # Handle client-specific errors
    print(f"ClientError occurred: {e.response['Error']['Message']}")
except Exception as e:
    # Handle any unexpected errors
    print(f"An unexpected error occurred: {str(e)}")
