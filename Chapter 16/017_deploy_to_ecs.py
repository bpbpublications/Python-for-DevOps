# Script: 017_deploy_to_ecs.py

import boto3

def deploy_to_ecs(cluster_name, service_name, task_definition):
    """
    Registers a task definition and updates an ECS service with the new task definition.

    :param cluster_name: The name of the ECS cluster.
    :param service_name: The name of the ECS service to update.
    :param task_definition: The task definition family name to register.
    """
    ecs_client = boto3.client('ecs')

    print("Registering task definition...")
    # Register a new task definition in ECS
    response = ecs_client.register_task_definition(
        family=task_definition,  # The task definition family
        containerDefinitions=[{
            "name": "django-backend",      # Container name
            "image": "django-backend:latest",  # Container image
            "memory": 512,                  # Memory in MB
            "cpu": 256,                     # CPU units
            "essential": True,              # Mark this container as essential
            "portMappings": [{
                "containerPort": 8000,      # Container port
                "hostPort": 8000            # Host port (for access to the container)
            }]
        }]
    )

    # Retrieve the ARN of the registered task definition
    task_definition_arn = response['taskDefinition']['taskDefinitionArn']
    print(f"Task definition registered: {task_definition_arn}")

    print("Updating ECS service...")
    # Update the ECS service with the new task definition ARN
    ecs_client.update_service(
        cluster=cluster_name,
        service=service_name,
        taskDefinition=task_definition_arn
    )

    print(f"Deployment to ECS service {service_name} completed.")

if __name__ == "__main__":
    # Example: Deploy to ECS with the cluster name, service name, and task definition
    deploy_to_ecs("MyCluster", "MyService", "django-backend-task")
