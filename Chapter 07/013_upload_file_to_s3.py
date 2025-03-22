# Script: 013_upload_file_to_s3.py

import boto3  # Import Boto3

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    Args:
        file_name (str): Path to the file to upload.
        bucket_name (str): S3 bucket name.
        object_name (str, optional): S3 object name. If not specified, file_name is used.
    """
    if object_name is None:
        object_name = file_name

    try:
        # Initialize S3 client
        s3 = boto3.client('s3')# Script: 014_dynamodb_dynamic_capacity.py

import boto3

def calculate_capacity_units(expected_read_ops, expected_write_ops):
    """
    Dynamically calculate read and write capacity units based on expected workload.

    Args:
        expected_read_ops (int): Expected read operations per second.
        expected_write_ops (int): Expected write operations per second.

    Returns:
        tuple: Read and write capacity units.
    """
    # Assuming a base unit of 1 read or write per second per unit
    read_capacity = max(1, expected_read_ops // 10)  # Example scaling factor for reads
    write_capacity = max(1, expected_write_ops // 5)  # Example scaling factor for writes
    return read_capacity, write_capacity

# Expected workload (can come from monitoring or predictions)
expected_read_ops = 500  # Expected read operations per second
expected_write_ops = 200  # Expected write operations per second

# Calculate capacity units based on workload
read_capacity, write_capacity = calculate_capacity_units(expected_read_ops, expected_write_ops)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create DynamoDB table with calculated capacity
try:
    table = dynamodb.create_table(
        TableName='MySampleTable',
        KeySchema=[
            {'AttributeName': 'username', 'KeyType': 'HASH'},  # Partition key
            {'AttributeName': 'last_name', 'KeyType': 'RANGE'}  # Sort key
        ],
        AttributeDefinitions=[
            {'AttributeName': 'username', 'AttributeType': 'S'},  # String type
            {'AttributeName': 'last_name', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': read_capacity,
            'WriteCapacityUnits': write_capacity
        }
    )
    print(f"Table MySampleTable is being created with {read_capacity} ReadCapacityUnits and {write_capacity} WriteCapacityUnits.")
    table.wait_until_exists()  # Wait until the table is fully created
except Exception as e:
    print(f"Error creating table: {e}")

# Insert item into table
try:
    table.put_item(Item={
        'username': 'janedoe',
        'last_name': 'Doe',
        'age': 29,
        'email': 'janedoe@example.com'
    })
    print("Item inserted.")
except Exception as e:
    print(f"Error inserting item: {e}")

# Query table for the item
try:
    item = table.get_item(Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }).get('Item')
    print("Query response:", item)
except Exception as e:
    print(f"Error querying item: {e}")

        
        # Upload file to the specified bucket
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"{file_name} uploaded to {bucket_name} as {object_name}.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

# Example usage
if __name__ == "__main__":
    upload_file_to_s3('myfile.txt', 'mybucket')
