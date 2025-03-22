# Script: 025_create_ec2_instance.py

import boto3

def create_ec2_instance(image_id, instance_type, key_name, min_count=1, max_count=1):
    """
    Creates an EC2 instance with the specified parameters.

    Args:
        image_id (str): The AMI ID for the instance.
        instance_type (str): The instance type (e.g., 't2.micro').
        key_name (str): The name of the key pair to associate with the instance.
        min_count (int, optional): Minimum number of instances to create. Default is 1.
        max_count (int, optional): Maximum number of instances to create. Default is 1.

    Returns:
        list: A list of created EC2 instance objects.
    """
    try:
        ec2 = boto3.resource('ec2')
        instances = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=min_count,
            MaxCount=max_count
        )
        return instances
    except Exception as e:
        print(f"An error occurred while creating the EC2 instance: {e}")
        return []

# Example usage
if __name__ == "__main__":
    instance = create_ec2_instance('ami-0abcdef1234567890', 't2.micro', 'MyKeyPair')
    if instance:
        print(f'Created instance: {instance[0].id}')
