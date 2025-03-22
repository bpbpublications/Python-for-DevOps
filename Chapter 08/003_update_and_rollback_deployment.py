# Script: 003_update_and_rollback_deployment.py

import time
from kubernetes import client, config, watch

# Load Kubernetes configuration and initialize the AppsV1 API client
config.load_kube_config()
v1 = client.AppsV1Api()

# Deployment and namespace details
deployment_name, namespace = 'my-deployment', 'default'

# Update deployment to a new image
def update_deployment(new_image):
    """
    Updates the deployment to use a new container image.

    Args:
        new_image (str): The new container image to use.
    """
    deployment = v1.read_namespaced_deployment(deployment_name, namespace)
    deployment.spec.template.spec.containers[0].image = new_image
    v1.replace_namespaced_deployment(deployment_name, namespace, deployment)
    print(f"Deployment updated to image {new_image}")

# Check if the deployment is healthy
def is_deployment_healthy():
    """
    Monitors the deployment's status to determine if it is healthy.

    Returns:
        bool: True if the deployment is healthy, False otherwise.
    """
    w = watch.Watch()
    try:
        for event in w.stream(v1.read_namespaced_deployment, deployment_name, namespace):
            cond = event['object'].status.conditions[-1]
            if cond.type == "Available" and cond.status == "True":
                print("Deployment is healthy")
                w.stop()
                return True
            if cond.type == "Progressing" and cond.status == "False":
                print("Deployment is unhealthy")
                w.stop()
                return False
    except Exception as e:
        print(f"Error while monitoring deployment health: {e}")
    finally:
        w.stop()

# Rollback deployment to the previous version
def rollback_deployment():
    """
    Rolls back the deployment to the previous version.
    """
    print("Rolling back deployment...")
    rollback_body = client.V1DeploymentRollback(
        name=deployment_name,
        rollback_to=client.V1RollbackConfig(revision=0)
    )
    v1.create_namespaced_deployment_rollback(name=deployment_name, namespace=namespace, body=rollback_body)
    print("Rollback complete")

# Main script
if __name__ == "__main__":
    new_image = "your-application-image:new-version"  # Replace with the desired new image
    try:
        update_deployment(new_image)
        time.sleep(30)  # Wait for the deployment to stabilize
        if not is_deployment_healthy():
            rollback_deployment()
    except client.rest.ApiException as e:
        print(f"ApiException: {e}")  # Handle Kubernetes API exceptions
    except KeyboardInterrupt:
        print("Script interrupted")  # Graceful shutdown on keyboard interrupt
