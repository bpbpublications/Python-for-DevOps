# Script: 018_create_gcp_instance.py

from google.cloud import compute_v1
from google.oauth2 import service_account
from google.api_core.exceptions import GoogleAPICallError, NotFound, PermissionDenied

try:
    # Authenticate using service account credentials
    credentials = service_account.Credentials.from_service_account_file('path/to/your/service-account-key.json')
    compute_client = compute_v1.InstancesClient(credentials=credentials)

    # Parameters for the VM instance
    project = "your-gcp-project-id"  # Replace with your GCP project ID
    zone = "us-central1-a"  # Specify the desired zone
    machine_type = f"zones/{zone}/machineTypes/n1-standard-1"  # Define machine type
    name = "your-instance-name"  # Replace with your desired instance name

    # Configure the VM instance
    instance = compute_v1.Instance()
    instance.name = name
    instance.zone = zone
    instance.machine_type = machine_type

    # Set up the boot disk
    disk = compute_v1.AttachedDisk()
    disk.initialize_params = compute_v1.AttachedDiskInitializeParams(
        source_image="projects/debian-cloud/global/images/family/debian-10"  # Debian 10 image
    )
    disk.auto_delete = True
    disk.boot = True
    instance.disks = [disk]

    # Set up the network interface
    network_interface = compute_v1.NetworkInterface()
    instance.network_interfaces = [network_interface]

    # Create the VM instance
    try:
        operation = compute_client.insert(project=project, zone=zone, instance_resource=instance)
        print(f"Instance creation initiated: {operation.name}")
    except GoogleAPICallError as e:
        print(f"Error during instance creation: {e.message}")

    # List instances in the zone
    try:
        instances = compute_client.list(project=project, zone=zone)
        for vm in instances:
            print(f"Instance name: {vm.name}, Status: {vm.status}")
    except NotFound:
        print("Error: The specified project or zone was not found.")
    except PermissionDenied:
        print("Error: Permission denied. Check your service account permissions.")
    except GoogleAPICallError as e:
        print(f"Error during instance listing: {e.message}")

except FileNotFoundError:
    print("Error: Service account key file not found. Please provide a valid file path.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
