# Script: 006_manage_ec2_instances.py

import boto3

# Initialize a Boto3 EC2 client
ec2 = boto3.client('ec2')

def manage_ec2_instances(action):
    """
    Manage EC2 instances based on the specified action ('start' or 'stop').

    Args:
        action (str): The action to perform ('start' or 'stop').
    """
    try:
        # Define filters to find instances tagged with 'Environment=Dev'
        filters = [{'Name': 'tag:Environment', 'Values': ['Dev']}]
        
        # Describe instances matching the filters
        instances = ec2.describe_instances(Filters=filters)
        
        # Extract instance IDs from the response
        instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
        
        if instance_ids:
            if action == 'start':
                # Start the instances
                ec2.start_instances(InstanceIds=instance_ids)
                print("Started instances:", instance_ids)
            elif action == 'stop':
                # Stop the instances
                ec2.stop_instances(InstanceIds=instance_ids)
                print("Stopped instances:", instance_ids)
            else:
                # Handle invalid actions
                print(f"Invalid action: {action}. Please use 'start' or 'stop'.")
        else:
            print("No instances found matching the filters.")
    except Exception as e:
        # Handle exceptions
        print(f"Error managing instances: {e}")

# Example usage
if __name__ == '__main__':
    manage_ec2_instances('start')  # Start instances
    manage_ec2_instances('stop')   # Stop instances
