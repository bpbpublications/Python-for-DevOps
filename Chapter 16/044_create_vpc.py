# Script: 044_create_vpc.py

import boto3

def create_vpc(cidr_block):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.create_vpc(CidrBlock=cidr_block)
        vpc_id = response['Vpc']['VpcId']
        print(f"VPC created. ID: {vpc_id}")
        return vpc_id
    except Exception as e:
        print(f"Error creating VPC: {e}")
        return None

if __name__ == "__main__":
    create_vpc("10.0.0.0/16")
