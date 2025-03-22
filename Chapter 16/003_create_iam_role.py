# Script: 003_create_iam_role.py

import boto3
import json

def create_iam_role(role_name):
    """
    Creates an IAM role with a trust relationship policy allowing EC2 service to assume the role.
    
    :param role_name: The name of the IAM role to be created
    :return: The ARN of the created role, or None if an error occurred
    """
    # Initialize the IAM client
    iam = boto3.client('iam')

    # Define the trust relationship policy document
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    # Attempt to create the IAM role
    try:
        response = iam.create_role(
            RoleName=role_name,  # Name of the role to be created
            AssumeRolePolicyDocument=json.dumps(trust_policy),  # Convert policy to JSON string
            Description="Role for EC2 to access other AWS services"  # Description of the role
        )
        print(f"Role '{role_name}' created successfully.")
        return response['Role']['Arn']  # Return the ARN of the created role
    except Exception as e:
        print(f"Error creating role: {e}")
        return None

# Example usage (Uncomment and replace 'your_role_name' to test)
# role_arn = create_iam_role('your_role_name')
# print(f"Created Role ARN: {role_arn}")
