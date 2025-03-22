# Script: 050_scale_ec2_instances.py

import boto3

def scale_ec2_instances(asg_name, desired_capacity):
    asg_client = boto3.client('autoscaling')
    try:
        response = asg_client.set_desired_capacity(
            AutoScalingGroupName=asg_name,
            DesiredCapacity=desired_capacity,
            HonorCooldown=True
        )
        print(f"Auto-scaling group {asg_name} updated to {desired_capacity} instances.")
    except Exception as e:
        print(f"Error scaling EC2 instances: {e}")

if __name__ == "__main__":
    scale_ec2_instances("my-asg", 5)
