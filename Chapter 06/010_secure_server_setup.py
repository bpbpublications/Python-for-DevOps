# Script: 010_secure_server_setup.py

import subprocess

def run_command(command):
    """
    Executes a shell command and prints its output.
    If an error occurs, it prints the error message.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def update_ssh_config():
    """
    Updates the SSH configuration file with custom security settings.
    Creates a backup of the SSH configuration file before modifying it.
    """
    ssh_config_file = '/etc/ssh/sshd_config'
    try:
        # Backup the SSH config file
        run_command(f"cp {ssh_config_file} {ssh_config_file}.bak")
        print(f"Backup created: {ssh_config_file}.bak")
        
        # Add or modify SSH configuration settings
        with open(ssh_config_file, 'a') as file:
            file.write("\n# Custom security settings\n")
            file.write("PermitRootLogin no\n")
            file.write("PasswordAuthentication no\n")
            file.write("Port 2222\n")
        print(f"SSH configuration updated: {ssh_config_file}")
        
        # Restart SSH service to apply changes
        run_command("systemctl restart sshd")
        print("SSH service restarted.")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An unexpected error occurred while updating SSH configuration: {e}")

def setup_basic_firewall():
    """
    Sets up a basic firewall by blocking a specific IP address.
    Modify this function to include additional firewall rules as needed.
    """
    try:
        run_command("iptables -A INPUT -s 192.168.1.100 -j DROP")
        print("Firewall rule added to block IP: 192.168.1.100")
    except Exception as e:
        print(f"An error occurred while setting up the firewall: {e}")

def update_system_packages():
    """
    Updates and upgrades the system packages.
    """
    try:
        run_command("apt-get update")
        run_command("apt-get upgrade -y")
        print("System packages updated and upgraded.")
    except Exception as e:
        print(f"An error occurred while updating system packages: {e}")

if __name__ == "__main__":
    # Run security configuration functions
    try:
        update_ssh_config()
        setup_basic_firewall()
        update_system_packages()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
