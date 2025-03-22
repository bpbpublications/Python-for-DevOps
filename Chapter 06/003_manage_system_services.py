# Script: 003_manage_system_services.py

import subprocess

def run_command(command):
    """
    Executes a shell command and returns the output.
    Handles exceptions and returns stderr if an error occurs.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def start_service(service_name):
    """
    Starts a system service.
    """
    print(f"Starting {service_name}...")
    return run_command(f"sudo systemctl start {service_name}")

def stop_service(service_name):
    """
    Stops a system service.
    """
    print(f"Stopping {service_name}...")
    return run_command(f"sudo systemctl stop {service_name}")

def restart_service(service_name):
    """
    Restarts a system service.
    """
    print(f"Restarting {service_name}...")
    return run_command(f"sudo systemctl restart {service_name}")

def status_service(service_name):
    """
    Checks the status of a system service.
    """
    print(f"Checking status of {service_name}...")
    return run_command(f"sudo systemctl status {service_name}")

# Example usage
if __name__ == "__main__":
    service = 'apache2'  # Replace with your service name
    try:
        print(start_service(service))
        print(status_service(service))
        print(restart_service(service))
        print(stop_service(service))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
