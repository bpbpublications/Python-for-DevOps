# Script: 002_setup_aws_resources.py

import os
from python_terraform import Terraform

def setup_aws_resources():
    """
    Sets up AWS resources using Terraform.
    """
    # Set up environment variables for AWS credentials
    os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key'  # Replace with your actual AWS access key
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_key'  # Replace with your actual AWS secret key

    # Initialize Terraform in the specified working directory
    tf = Terraform(working_dir="./terraform")
    tf.init()  # Initialize Terraform configurations

    # Plan Terraform execution
    print("Planning infrastructure...")
    tf.plan()  # Generate and show the execution plan

    # Apply the Terraform plan to create/update resources
    print("Applying configuration...")
    tf.apply(skip_plan=True)  # Apply the changes without prompting for confirmation

    print("AWS resources have been successfully set up.")

if __name__ == "__main__":
    setup_aws_resources()
