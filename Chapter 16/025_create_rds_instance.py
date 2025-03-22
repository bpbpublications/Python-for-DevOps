# Script: 025_create_rds_instance.py

import boto3

def create_rds_instance(db_instance_identifier, db_name, username, password):
    rds_client = boto3.client('rds')
    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            DBName=db_name,
            MasterUsername=username,
            MasterUserPassword=password,
            DBInstanceClass='db.t2.micro',
            Engine='postgres',
            AllocatedStorage=20
        )
        print(f"RDS instance '{db_instance_identifier}' is being created.")
        print(response)
    except Exception as e:
        print(f"Error creating RDS instance: {e}")

if __name__ == "__main__":
    create_rds_instance(
        db_instance_identifier="my-postgres-db",
        db_name="mydb",
        username="admin",
        password="password123"
    )
