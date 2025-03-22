# Script: 001_ssh_command_executor.py

import paramiko
import os

# Fetching environment variables for SSH connection
hostname = os.getenv('SSH_HOST')
username = os.getenv('SSH_USER')
password = os.getenv('SSH_PASS')
port = 22  # Default SSH port is 22

# Command to be executed on the remote server
command = 'ls -l'

# Creating an SSH client instance
client = paramiko.SSHClient()

# Automatically adding the server's host key 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Ensure environment variables are not None
    if not hostname or not username or not password:
        raise ValueError("SSH connection parameters are missing. Check environment variables.")
    
    # Connecting to the server
    client.connect(hostname=hostname, port=port, username=username, password=password)
    print(f"Successfully connected to {hostname}")
    
    # Executing the command
    stdin, stdout, stderr = client.exec_command(command)
    print("Command executed, output:")
    
    # Reading the standard output
    for line in stdout:
        print(line.strip())
    
    # Reading the standard error if any
    errors = stderr.read().decode('utf-8')
    if errors:
        print(f"Errors during command execution: {errors}")

except ValueError as ve:
    print(f"Parameter Error: {ve}")

except paramiko.AuthenticationException as auth_exc:
    print(f"Authentication failed: {auth_exc}")

except Exception as e:
    print(f"Connection failed: {e}")

finally:
    # Closing the client connection
    client.close()
    print("Connection closed")
