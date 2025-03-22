# Script: 004_ssh_network_device.py

import paramiko
import os  # For SSH and environment variables

# Hostname of the network device
hostname = "network-device"

# Retrieve credentials from environment variables (consider using a secret manager for production)
username = os.getenv("SSH_USERNAME")
password = os.getenv("SSH_PASSWORD")

# Create an SSH client
ssh_client = paramiko.SSHClient()
# Set policy to automatically add the server's host key (not recommended for production)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the network device via SSH
    ssh_client.connect(hostname, username=username, password=password)
    
    # Execute a command on the remote device
    stdin, stdout, stderr = ssh_client.exec_command("show ip interface brief")
    
    # Print the output of the command
    print(f"Connected to {hostname}\n{stdout.read().decode()}")
    
    # Close the SSH connection
    ssh_client.close()
except paramiko.AuthenticationException:
    # Handle authentication errors
    print("Authentication failed.")
except paramiko.SSHException as e:
    # Handle SSH-specific errors
    print(f"SSH error: {e}")
except Exception as e:
    # Handle general errors
    print(f"Error: {e}")
