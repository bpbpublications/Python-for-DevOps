# Script: 042_manage_systemd_service.py
# Purpose: Demonstrates how to manage systemd services using the `subprocess` module.

import subprocess

def manage_service(service_name, action):
    """
    Manage a systemd service (e.g., start, stop, restart, status).

    Args:
        service_name (str): The name of the systemd service (e.g., 'apache2').
        action (str): The action to perform on the service ('start', 'stop', 'restart', 'status').

    Raises:
        subprocess.CalledProcessError: If the systemctl command fails.
    """
    try:
        # Run the systemctl command with the specified action on the given service
        subprocess.run(['sudo', 'systemctl', action, service_name], check=True)
        print(f"Service '{service_name}' {action}ed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle failure of the systemctl command
        print(f"Failed to {action} service '{service_name}'. Error: {e}")

# Main program logic
if __name__ == "__main__":
    # Example usage of managing system services
    manage_service('apache2', 'start')  # Starting Apache service
    manage_service('apache2', 'stop')   # Stopping Apache service
