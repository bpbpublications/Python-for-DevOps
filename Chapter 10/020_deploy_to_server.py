# Script: 020_deploy_to_server.py

import paramiko

def deploy_to_server():
    """
    Deploys an application to a remote server via SSH. The process involves:
    1. Connecting to the remote server using SSH.
    2. Uploading the application artifacts (e.g., a tarball).
    3. Executing a deployment script on the remote server.
    4. Closing the SSH connection.
    """
    try:
        # Connect to remote server via SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='example.com', username='user', password='password')

        # Upload application artifacts to remote server
        ftp_client = ssh_client.open_sftp()
        ftp_client.put('app.tar.gz', '/path/to/remote/app.tar.gz')  # Replace with actual file and remote path
        ftp_client.close()

        # Execute deployment script on remote server
        stdin, stdout, stderr = ssh_client.exec_command('bash /path/to/remote/deploy.sh')  # Replace with actual script path

        # Print output and errors from the deployment script
        print(stdout.read().decode())
        print(stderr.read().decode())

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection error: {e}")
    except Exception as e:
        print(f"Error during deployment: {e}")
    finally:
        # Ensure the SSH connection is closed
        ssh_client.close()

# Invoke the deployment function when the script is executed
if __name__ == "__main__":
    deploy_to_server()
