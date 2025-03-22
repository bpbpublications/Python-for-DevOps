# Script: 016_create_rds_instance.py

import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Initialize RDS client
rds_client = boto3.client('rds')

try:
    # Create RDS instance
    response = rds_client.create_db_instance(
        DBInstanceIdentifier='mydbinstance',
        AllocatedStorage=20,  # Specify storage size in GB
        DBInstanceClass='db.t2.micro',  # Specify instance class
        Engine='MySQL',  # Specify database engine
        MasterUsername=os.getenv('DB_USERNAME'),  # Fetch DB username from environment variables
        MasterUserPassword=os.getenv('DB_PASSWORD')  # Fetch DB password from environment variables
    )
    # Print response for confirmation
    print("RDS instance creation initiated:", response)

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
