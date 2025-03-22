# Script: 049_perform_rolling_update.py

import boto3

def perform_rolling_update(cluster_name, service_name, task_definition):
    ecs_client = boto3.client('ecs')
    try:
        ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            taskDefinition=task_definition,
            deploymentConfiguration={
                'maximumPercent': 200,
                'minimumHealthyPercent': 50
            }
        )
        print(f"Rolling update initiated for service {service_name}.")
    except Exception as e:
        print(f"Error during rolling update: {e}")

if __name__ == "__main__":
    perform_rolling_update("my-cluster", "my-service", "my-task-def:2")
