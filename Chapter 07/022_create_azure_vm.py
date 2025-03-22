# Script: 022_create_azure_vm.py

import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachine, HardwareProfile, NetworkProfile, NetworkInterfaceReference, OSProfile, VirtualMachineSizeTypes

# Get subscription ID from environment variables
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')

# Authenticate and create a ComputeManagementClient
compute_client = ComputeManagementClient(DefaultAzureCredential(), subscription_id)

# VM parameters
vm_params = VirtualMachine(
    location=os.getenv('AZURE_LOCATION'),
    os_profile=OSProfile(
        admin_username=os.getenv('VM_ADMIN_USER'),
        admin_password=os.getenv('VM_ADMIN_PASS'),  # Store sensitive data securely, e.g., Azure Key Vault
        computer_name=os.getenv('VM_NAME')
    ),
    hardware_profile=HardwareProfile(vm_size=VirtualMachineSizeTypes.standard_b2s),
    network_profile=NetworkProfile(
        network_interfaces=[
            NetworkInterfaceReference(
                id=f"/subscriptions/{subscription_id}/resourceGroups/{os.getenv('AZURE_RESOURCE_GROUP')}/providers/Microsoft.Network/networkInterfaces/{os.getenv('VM_NIC_NAME')}",
                primary=True
            )
        ]
    ),
    storage_profile={
        "image_reference": {
            "publisher": 'Canonical',
            "offer": 'UbuntuServer',
            "sku": '18.04-LTS',
            "version": 'latest'
        },
        "os_disk": {
            "caching": "ReadWrite",
            "managed_disk": {"storage_account_type": "Standard_LRS"},
            "name": "myosdisk1",
            "create_option": "FromImage"
        }
    }
)

try:
    # Create and start the VM
    compute_client.virtual_machines.begin_create_or_update(
        os.getenv('AZURE_RESOURCE_GROUP'),
        os.getenv('VM_NAME'),
        vm_params
    ).wait()
    compute_client.virtual_machines.begin_start(
        os.getenv('AZURE_RESOURCE_GROUP'),
        os.getenv('VM_NAME')
    ).wait()
    print("VM created and started successfully.")
except Exception as e:
    print(f"Error occurred while creating or starting the VM: {str(e)}")

# List all VMs in the subscription
try:
    for vm in compute_client.virtual_machines.list_all():
        print(f"VM name: {vm.name}")
except Exception as e:
    print(f"Error occurred while listing VMs: {str(e)}")
