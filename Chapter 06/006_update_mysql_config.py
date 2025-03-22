# Script: 006_update_mysql_config.py

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

def update_mysql_config(file_path, new_settings):
    """
    Updates the MySQL configuration file with the provided settings.
    Creates a backup before modifying the file.
    """
    try:
        # Create a backup of the configuration file
        backup_file(file_path)
        
        # Read the existing configuration file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Update the file content with new settings
        with open(file_path, 'w') as file:
            for line in lines:
                for setting, value in new_settings.items():
                    if line.startswith(setting):
                        line = f'{setting} = {value}\n'
                        break
                file.write(line)
            
            # Append new settings if they don't exist in the file
            for setting, value in new_settings.items():
                if not any(setting in line for line in lines):
                    file.write(f'{setting} = {value}\n')
        
        print(f"MySQL configuration updated: {file_path}")
    except FileNotFoundError:
        print(f"Configuration file not found: {file_path}")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define the file path and new settings
    mysql_config_file = '/etc/mysql/my.cnf'  # Replace with the path to your MySQL config file
    new_settings = {
        'innodb_buffer_pool_size': '1G',  # Adjust as per your server's requirements
        'max_connections': '500',
        'query_cache_size': '64M',
    }
    update_mysql_config(mysql_config_file, new_settings)
