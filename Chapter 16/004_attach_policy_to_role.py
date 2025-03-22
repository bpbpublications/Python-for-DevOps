# Script: 004_attach_policy_to_role.py

import boto3

def attach_policy_to_role(role_name, policy_arn):
    """
    Attaches an IAM policy to a specified IAM role.
    
    :param role_name: The name of the IAM role
    :param policy_arn: The ARN of the IAM policy to attach
    """
    # Initialize the IAM client
    iam = boto3.client('iam')

    try:
        # Attach the policy to the role
        iam.attach_role_policy(
            RoleName=role_name,  # Name of the role
            PolicyArn=policy_arn  # ARN of the policy to attach
        )
        print(f"Policy '{policy_arn}' attached to role '{role_name}'.")
    except Exception as e:
        print(f"Error attaching policy: {e}")

# Example usage (Uncomment and replace with your values to test)
# attach_policy_to_role('your_role_name', 'arn:aws:iam::aws:policy/YourPolicyName')
