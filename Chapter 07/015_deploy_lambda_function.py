# Script: 015_deploy_lambda_function.py

import boto3
import zipfile
import io

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Prepare the zip file containing the Lambda function code
zip_buffer = io.BytesIO()
try:
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write('lambda_function.py')  # Replace with your Lambda function code file path
    zip_buffer.seek(0)
except Exception as e:
    print(f"Error creating zip file: {e}")
    exit(1)

# Deploy the Lambda function
try:
    response = lambda_client.create_function(
        FunctionName='MyLambdaFunction',  # Set the name for your Lambda function
        Runtime='python3.8',  # Define the runtime for the Lambda function
        Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with the actual IAM role ARN
        Handler='lambda_function.lambda_handler',  # Replace with the actual handler name
        Code={'ZipFile': zip_buffer.getvalue()}  # Provide the zipped function code
    )

    # Print the function's ARN as confirmation
    print(f"Lambda function deployed: {response['FunctionArn']}")
except Exception as e:
    print(f"Error deploying Lambda function: {e}")
