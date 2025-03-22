# Script: 047_create_rds_snapshot.py

import boto3

def create_rds_snapshot(db_instance_id, snapshot_identifier):
    rds_client = boto3.client('rds')
    try:
        response = rds_client.create_db_snapshot(
            DBInstanceIdentifier=db_instance_id,
            DBSnapshotIdentifier=snapshot_identifier
        )
        print(f"RDS snapshot created: {response['DBSnapshot']['DBSnapshotIdentifier']}")
    except Exception as e:
        print(f"Error creating RDS snapshot: {e}")

if __name__ == "__main__":
    create_rds_snapshot("your-db-instance-id", "my-db-backup")
