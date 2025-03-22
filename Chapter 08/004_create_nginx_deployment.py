# Script: 004_create_nginx_deployment.py

from kubernetes import client, config

def create_deployment_object():
    """
    Creates a Kubernetes deployment object for an NGINX application.

    Returns:
        V1Deployment: A deployment object configured for NGINX.
    """
    # Define the container specification
    container = client.V1Container(
        name="nginx",
        image="nginx:1.17",
        ports=[client.V1ContainerPort(container_port=80)]
    )

    # Define the pod template specification
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container])
    )

    # Define the deployment specification
    spec = client.V1DeploymentSpec(
        replicas=3,
        template=template,
        selector={'matchLabels': {'app': 'nginx'}}
    )

    # Create and return the deployment object
    return client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="nginx-deployment"),
        spec=spec
    )

def create_deployment(api_instance, deployment):
    """
    Creates a Kubernetes deployment in the 'default' namespace.

    Args:
        api_instance (AppsV1Api): Kubernetes AppsV1 API instance.
        deployment (V1Deployment): The deployment object to be created.
    """
    api_instance.create_namespaced_deployment(body=deployment, namespace="default")
    print("Deployment created successfully.")

# Load the Kubernetes configuration and create the deployment
if __name__ == "__main__":
    config.load_kube_config()  # Load kubeconfig file to access the cluster
    apps_v1 = client.AppsV1Api()  # Initialize AppsV1 API instance
    deployment = create_deployment_object()  # Create the deployment object
    create_deployment(apps_v1, deployment)  # Deploy the NGINX application
