# Script: 001_kubernetes_pod_management.py

import time
from kubernetes import client, config, watch

# Load Kubernetes configuration and initialize the CoreV1 API client
config.load_kube_config()
v1 = client.CoreV1Api()

# Define pod specifications using Kubernetes client models
pod_manifest = client.V1Pod(
    api_version="v1",
    kind="Pod",
    metadata=client.V1ObjectMeta(name="mypod"),
    spec=client.V1PodSpec(
        containers=[
            client.V1Container(
                name="mycontainer",
                image="nginx"  # Image to use for the container
            )
        ]
    )
)

# Function to create a pod
def create_pod():
    """
    Creates a pod in the 'default' namespace using the pod_manifest.
    """
    v1.create_namespaced_pod(namespace="default", body=pod_manifest)
    print("Pod created")

# Function to monitor the pod's status
def monitor_pod():
    """
    Monitors the pod until its status changes to 'Running'.
    """
    w = watch.Watch()
    try:
        for event in w.stream(v1.list_namespaced_pod, namespace="default"):
            pod = event['object']
            if pod.metadata.name == "mypod" and pod.status.phase == "Running":
                print(f"Pod {pod.metadata.name} is running")
                w.stop()
    except client.rest.ApiException as e:
        print(f"Error while monitoring pod: {e}")
    finally:
        w.stop()

# Function to delete the pod
def delete_pod():
    """
    Deletes the pod named 'mypod' from the 'default' namespace.
    """
    v1.delete_namespaced_pod(name="mypod", namespace="default", body=client.V1DeleteOptions())
    print("Pod deleted")

# Main script to orchestrate the pod lifecycle
if __name__ == "__main__":
    try:
        create_pod()  # Create the pod
        monitor_pod()  # Monitor its status
        time.sleep(10)  # Allow the pod to run for a short time
        delete_pod()  # Delete the pod
    except client.rest.ApiException as e:
        print(f"ApiException occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
