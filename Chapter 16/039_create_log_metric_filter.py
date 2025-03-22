# Script: 039_create_log_metric_filter.py

import boto3

def create_log_metric_filter(log_group_name, filter_name, pattern, metric_name, namespace):
    logs_client = boto3.client('logs')
    try:
        logs_client.put_metric_filter(
            logGroupName=log_group_name,
            filterName=filter_name,
            filterPattern=pattern,
            metricTransformations=[
                {
                    'metricName': metric_name,
                    'metricNamespace': namespace,
                    'metricValue': "1"
                }
            ]
        )
        print(f"Log metric filter '{filter_name}' created successfully.")
    except Exception as e:
        print(f"Error creating log metric filter: {e}")

if __name__ == "__main__":
    create_log_metric_filter(
        log_group_name="my-app-logs",
        filter_name="ErrorFilter",
        pattern="ERROR",
        metric_name="ErrorCount",
        namespace="MyAppNamespace"
    )
