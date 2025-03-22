# Script: 026_configure_rds_backup_and_monitoring.py

import boto3

def configure_rds_backup_and_monitoring(db_instance_identifier):
    rds_client = boto3.client('rds')
    try:
        rds_client.modify_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            BackupRetentionPeriod=7,  # Retain backups for 7 days
            CloudwatchLogsExports=['postgresql'],
            MonitoringInterval=60  # Enable enhanced monitoring
        )
        print(f"Backup and monitoring enabled for RDS instance '{db_instance_identifier}'.")
    except Exception as e:
        print(f"Error configuring backups and monitoring: {e}")

if __name__ == "__main__":
    configure_rds_backup_and_monitoring("my-postgres-db")
