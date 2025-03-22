# Script: 005_scale_deployment.py

from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()
apps_v1 = client.AppsV1Api()

# Function to scale a deployment
def scale_deployment(deployment_name, namespace, replicas):
    """
    Scales the specified Kubernetes deployment to the desired number of replicas.

    Args:
        deployment_name (str): The name of the deployment to scale.
        namespace (str): The namespace of the deployment.
        replicas (int): The desired number of replicas.
    """
    # Create a scale object and set the desired number of replicas
    scale = client.V1Scale(
        spec=client.V1ScaleSpec(replicas=replicas)
    )
    
    # Update the deployment's scale
    apps_v1.patch_namespaced_deployment_scale(deployment_name, namespace, scale)
    print(f"Deployment '{deployment_name}' scaled to {replicas} replicas.")

# Example usage
if __name__ == "__main__":
    scale_deployment('my-deployment', 'default', 3)  # Scale the deployment to 3 replicas
