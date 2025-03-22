# Script: 043_create_and_manage_security_group.py

import boto3

def create_security_group(vpc_id, group_name, description):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )
        print(f"Security group {group_name} created. ID: {response['GroupId']}")
        return response['GroupId']
    except Exception as e:
        print(f"Error creating security group: {e}")
        return None

def add_security_group_rule(group_id, protocol, port, cidr):
    ec2_client = boto3.client('ec2')
    try:
        ec2_client.authorize_security_group_ingress(
            GroupId=group_id,
            IpProtocol=protocol,
            FromPort=port,
            ToPort=port,
            CidrIp=cidr
        )
        print(f"Rule added to security group {group_id}: {protocol} on port {port} for {cidr}.")
    except Exception as e:
        print(f"Error adding rule: {e}")

if __name__ == "__main__":
    sg_id = create_security_group("your-vpc-id", "MySecurityGroup", "Description of the group")
    if sg_id:
        add_security_group_rule(sg_id, "tcp", 22, "0.0.0.0/0")  # Example: Allow SSH
