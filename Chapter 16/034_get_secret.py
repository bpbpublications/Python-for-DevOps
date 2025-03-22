# Script: 034_get_secret.py

import boto3

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        print(f"Retrieved secret: {secret}")
        return secret
    except Exception as e:
        print(f"Error retrieving secret: {e}")

if __name__ == "__main__":
    get_secret("MyDatabasePassword")
