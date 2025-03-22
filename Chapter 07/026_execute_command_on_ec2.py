# Script: 026_execute_command_on_ec2.py

import os
import paramiko

# EC2 details from environment
host = os.getenv('EC2_HOST')  # Replace with the environment variable storing the EC2 host
username = 'ec2-user'  # Default username for Amazon Linux instances
key_path = os.getenv('EC2_KEY_PATH')  # Replace with the environment variable storing the path to the private key

# Initialize SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the EC2 instance
    ssh_client.connect(hostname=host, username=username, key_filename=key_path)
    print("Connected to the instance")
    
    # Execute a command on the EC2 instance
    stdin, stdout, stderr = ssh_client.exec_command('sudo apt-get update')
    print(stdout.read().decode())  # Output of the command
    print(stderr.read().decode())  # Errors (if any)
    
    # Close the connection
    ssh_client.close()
    print("Connection closed")
except Exception as e:
    print(f"Connection failed: {e}")
