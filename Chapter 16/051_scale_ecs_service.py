# Script: 051_scale_ecs_service.py

import boto3

def scale_ecs_service(cluster_name, service_name, desired_count):
    ecs_client = boto3.client('ecs')
    try:
        ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            desiredCount=desired_count
        )
        print(f"Service {service_name} scaled to {desired_count} tasks.")
    except Exception as e:
        print(f"Error scaling ECS service: {e}")

if __name__ == "__main__":
    scale_ecs_service("my-cluster", "my-service", 3)
