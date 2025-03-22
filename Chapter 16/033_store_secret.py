# Script: 033_store_secret.py

import boto3

def store_secret(secret_name, secret_value):
    client = boto3.client('secretsmanager')
    try:
        response = client.create_secret(
            Name=secret_name,
            SecretString=secret_value
        )
        print(f"Secret {secret_name} created successfully.")
    except client.exceptions.ResourceExistsException:
        print(f"Secret {secret_name} already exists.")
    except Exception as e:
        print(f"Error storing secret: {e}")

if __name__ == "__main__":
    store_secret("MyDatabasePassword", '{"username": "admin", "password": "mypassword"}')
