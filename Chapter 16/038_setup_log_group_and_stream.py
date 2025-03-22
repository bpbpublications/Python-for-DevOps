# Script: 038_setup_log_group_and_stream.py

import boto3

def setup_log_group_and_stream(log_group_name, log_stream_name):
    logs_client = boto3.client('logs')
    try:
        logs_client.create_log_group(logGroupName=log_group_name)
        logs_client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
        print(f"Log group '{log_group_name}' and log stream '{log_stream_name}' created.")
    except Exception as e:
        print(f"Error setting up log group and stream: {e}")

if __name__ == "__main__":
    setup_log_group_and_stream("my-app-logs", "app-stream")
