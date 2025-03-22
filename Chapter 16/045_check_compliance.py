# Script: 045_check_compliance.py

import boto3

def check_compliance(resource_id):
    config_client = boto3.client('config')
    try:
        response = config_client.get_compliance_details_by_resource(
            ResourceType='AWS::EC2::Instance',
            ResourceId=resource_id
        )
        print(f"Compliance details for {resource_id}: {response['EvaluationResults']}")
    except Exception as e:
        print(f"Error checking compliance: {e}")

if __name__ == "__main__":
    check_compliance("your-instance-id")
