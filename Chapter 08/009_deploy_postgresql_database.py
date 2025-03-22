# Script: 009_deploy_postgresql_database.py

from kubernetes import client, config

# Load Kubernetes configuration from the default location
config.load_kube_config()

def deploy_database():
    """
    Deploys a PostgreSQL database to a Kubernetes cluster using a Deployment.
    """
    # Initialize the AppsV1Api instance
    api_instance = client.AppsV1Api()

    # Define the PostgreSQL deployment using Kubernetes client models
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="postgresql-deployment"),
        spec=client.V1DeploymentSpec(
            replicas=1,  # Number of replicas
            selector=client.V1LabelSelector(
                match_labels={"app": "postgresql"}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "postgresql"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="postgres",  # Name of the container
                            image="postgres:latest",  # Image to use
                            ports=[
                                client.V1ContainerPort(container_port=5432)  # Expose port 5432
                            ],
                            env=[
                                client.V1EnvVar(name="POSTGRES_DB", value="exampledb"),  # Database name
                                client.V1EnvVar(name="POSTGRES_USER", value="exampleuser"),  # Database user
                                client.V1EnvVar(name="POSTGRES_PASSWORD", value="examplepass")  # Database password
                            ]
                        )
                    ]
                )
            )
        )
    )

    # Create the deployment in the 'default' namespace
    api_instance.create_namespaced_deployment(
        body=deployment, namespace="default"
    )

    print("Database deployed successfully.")

# Deploy the PostgreSQL database
if __name__ == "__main__":
    deploy_database()
