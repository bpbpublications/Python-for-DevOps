# Script: 007_update_ansible_config.py

import os

def backup_file(file_path):
    """
    Creates a backup of the given file by appending '.bak' to its name.
    """
    try:
        backup_path = file_path + '.bak'
        os.system(f'cp {file_path} {backup_path}')
        print(f"Backup created: {backup_path}")
    except Exception as e:
        print(f"Failed to create backup for {file_path}: {e}")

def update_ansible_config(file_path, new_settings):
    """
    Updates the Ansible configuration file with the provided settings.
    Creates a backup before modifying the file.
    """
    try:
        # Create a backup of the configuration file
        backup_file(file_path)
        
        # Read the existing configuration file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Update existing settings or note them for addition
        settings_to_add = new_settings.copy()
        with open(file_path, 'w') as file:
            for line in lines:
                for setting, value in new_settings.items():
                    if line.strip().startswith(setting):
                        line = f'{setting} = {value}\n'
                        settings_to_add.pop(setting, None)
                        break
                file.write(line)
            
            # Add new settings that were not found in the file
            for setting, value in settings_to_add.items():
                file.write(f'{setting} = {value}\n')
        
        print(f"Ansible configuration updated: {file_path}")
    except FileNotFoundError:
        print(f"Configuration file not found: {file_path}")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define the file path and new settings
    ansible_config_file = '/etc/ansible/ansible.cfg'  # Replace with the path to your Ansible config file
    new_settings = {
        'forks': '100',
        'host_key_checking': 'False',
        'remote_user': 'myuser',
    }
    update_ansible_config(ansible_config_file, new_settings)
