# Script: 046_create_ec2_snapshot.py

import boto3

def create_ec2_snapshot(instance_id, description="Backup"):
    ec2_client = boto3.client('ec2')
    try:
        volumes = ec2_client.describe_volumes(
            Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}]
        )['Volumes']

        for volume in volumes:
            snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId'],
                Description=description
            )
            print(f"Snapshot created: {snapshot['SnapshotId']} for volume {volume['VolumeId']}")
    except Exception as e:
        print(f"Error creating snapshot: {e}")

if __name__ == "__main__":
    create_ec2_snapshot("your-instance-id")
