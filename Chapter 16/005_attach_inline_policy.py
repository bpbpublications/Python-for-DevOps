# Script: 005_attach_inline_policy.py

import boto3
import json

def attach_inline_policy(role_name):
    """
    Attaches an inline policy to an IAM role, granting specific permissions.
    
    :param role_name: The name of the IAM role
    """
    # Initialize the IAM client
    iam = boto3.client('iam')

    # Define the inline policy
    inline_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",  # Allow listing the bucket
                    "s3:GetObject"    # Allow retrieving objects
                ],
                "Resource": [
                    "arn:aws:s3:::example-bucket",       # Access to the bucket
                    "arn:aws:s3:::example-bucket/*"     # Access to objects in the bucket
                ]
            }
        ]
    }

    try:
        # Attach the inline policy to the specified IAM role
        iam.put_role_policy(
            RoleName=role_name,  # Name of the role
            PolicyName="S3AccessPolicy",  # Name for the inline policy
            PolicyDocument=json.dumps(inline_policy)  # Convert policy to JSON string
        )
        print(f"Inline policy attached to role '{role_name}'.")
    except Exception as e:
        print(f"Error attaching inline policy: {e}")

# Example usage (Uncomment and replace 'your_role_name' with the actual role name to test)
# attach_inline_policy('your_role_name')
