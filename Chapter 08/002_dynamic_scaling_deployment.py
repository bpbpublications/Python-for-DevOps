# Script: 002_dynamic_scaling_deployment.py

import random
import time
from kubernetes import client, config

# Load Kubernetes configuration and initialize the AppsV1 API client
config.load_kube_config()
v1 = client.AppsV1Api()

# Deployment and namespace details
deployment_name, namespace = 'my-deployment', 'default'

# Simulate fetching custom metrics
def get_custom_metric():
    """
    Simulates fetching a custom metric value.
    Returns a random integer between 1 and 100.
    """
    return random.randint(1, 100)

# Scale deployment function using patch_namespaced_deployment_scale
def scale_deployment(replicas):
    """
    Scales the deployment to the specified number of replicas.
    
    Args:
        replicas (int): The desired number of replicas.
    """
    scale_body = {"spec": {"replicas": replicas}}
    v1.patch_namespaced_deployment_scale(name=deployment_name, namespace=namespace, body=scale_body)
    print(f"Scaled deployment '{deployment_name}' to {replicas} replicas")

# Main loop to check metrics and scale
if __name__ == "__main__":
    try:
        while True:
            # Fetch the current custom metric value
            metric = get_custom_metric()
            print(f"Metric value: {metric}")

            # Determine replica count based on metric
            if metric > 80:
                scale_deployment(5)  # Scale up
            elif metric < 20:
                scale_deployment(1)  # Scale down

            # Wait for 30 seconds before checking the metric again
            time.sleep(30)
    except client.rest.ApiException as e:
        print(f"ApiException: {e}")  # Handle Kubernetes API exceptions
    except KeyboardInterrupt:
        print("Script interrupted")  # Graceful shutdown on keyboard interrupt
