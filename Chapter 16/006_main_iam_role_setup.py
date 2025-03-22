# Script: 006_main_iam_role_setup.py

import boto3
import json

# Function to create an IAM role
def create_iam_role(role_name):
    """
    Creates an IAM role with a trust relationship policy allowing EC2 service to assume the role.
    """
    iam = boto3.client('iam')
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

    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Role for EC2 to access other AWS services"
        )
        print(f"Role '{role_name}' created successfully.")
        return response['Role']['Arn']
    except Exception as e:
        print(f"Error creating role: {e}")
        return None

# Function to attach a managed policy to a role
def attach_policy_to_role(role_name, policy_arn):
    """
    Attaches an IAM policy to a specified IAM role.
    """
    iam = boto3.client('iam')
    try:
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy '{policy_arn}' attached to role '{role_name}'.")
    except Exception as e:
        print(f"Error attaching policy: {e}")

# Function to attach an inline policy to a role
def attach_inline_policy(role_name):
    """
    Attaches an inline policy to an IAM role, granting specific permissions.
    """
    iam = boto3.client('iam')
    inline_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::example-bucket",
                    "arn:aws:s3:::example-bucket/*"
                ]
            }
        ]
    }

    try:
        iam.put_role_policy(
            RoleName=role_name,
            PolicyName="S3AccessPolicy",
            PolicyDocument=json.dumps(inline_policy)
        )
        print(f"Inline policy attached to role '{role_name}'.")
    except Exception as e:
        print(f"Error attaching inline policy: {e}")

if __name__ == "__main__":
    role_name = "MyEC2Role"  # Name of the role to create
    policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"  # ARN of the managed policy to attach

    # Create the role
    role_arn = create_iam_role(role_name)

    # Attach a managed policy if the role was created successfully
    if role_arn:
        attach_policy_to_role(role_name, policy_arn)

    # Attach a custom inline policy
    attach_inline_policy(role_name)
