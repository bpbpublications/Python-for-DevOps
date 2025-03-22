# Script: 040_create_dashboard.py

import boto3
import json

def create_dashboard(dashboard_name):
    cloudwatch = boto3.client('cloudwatch')
    dashboard_body = {
        "widgets": [
            {
                "type": "metric",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [["AWS/EC2", "CPUUtilization", "InstanceId", "i-1234567890"]],
                    "title": "CPU Utilization"
                }
            }
        ]
    }

    try:
        cloudwatch.put_dashboard(
            DashboardName=dashboard_name,
            DashboardBody=json.dumps(dashboard_body)
        )
        print(f"Dashboard '{dashboard_name}' created successfully.")
    except Exception as e:
        print(f"Error creating dashboard: {e}")

if __name__ == "__main__":
    create_dashboard("MyAppDashboard")
