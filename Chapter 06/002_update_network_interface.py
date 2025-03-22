# Script: 002_update_network_interface.py

import os
import shutil

# Network configuration settings
iface_name = 'eth0'  # Replace with your network interface name
static_ip = '192.168.1.100'  # Replace with your desired static IP
netmask = '255.255.255.0'
gateway = '192.168.1.1'  # Replace with your gateway address

# File paths
interfaces_file = '/etc/network/interfaces'
backup_file = '/etc/network/interfaces.bak'

try:
    # Ensure the original interfaces file exists
    if not os.path.exists(interfaces_file):
        raise FileNotFoundError(f"The file {interfaces_file} does not exist.")
    
    # Backup the original file
    shutil.copy(interfaces_file, backup_file)
    print(f"Backup created at {backup_file}")
    
    # Read the content of the original file
    with open(interfaces_file, 'r') as file:
        lines = file.readlines()
    
    # Prepare the new content
    new_content = []
    iface_found = False
    for line in lines:
        if line.startswith(f'iface {iface_name} '):
            iface_found = True
            new_content.append(f'iface {iface_name} inet static\n')
            new_content.append(f'    address {static_ip}\n')
            new_content.append(f'    netmask {netmask}\n')
            new_content.append(f'    gateway {gateway}\n')
        elif iface_found and line.startswith('    '):  # Skip indent lines of iface
            continue
        else:
            new_content.append(line)
            iface_found = False
    
    # Write the new content to the file
    with open(interfaces_file, 'w') as file:
        file.writelines(new_content)
    
    print("Network interfaces file has been updated.")

except FileNotFoundError as fnf_error:
    print(f"File Error: {fnf_error}")

except PermissionError:
    print("Permission denied. Run this script with elevated privileges (e.g., using sudo).")

except Exception as e:
    print(f"An error occurred: {e}")
