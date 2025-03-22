# Script: 005_update_bashrc.py

import os

def append_to_bashrc(line):
    """
    Appends a line to the user's .bashrc file if it does not already exist.
    Creates a backup of the .bashrc file before modifying it.
    """
    bashrc_path = os.path.expanduser('~/.bashrc')
    backup_path = os.path.expanduser('~/.bashrc.bak')

    try:
        # Check if .bashrc exists
        if not os.path.exists(bashrc_path):
            raise FileNotFoundError(f"{bashrc_path} does not exist. Cannot append line.")
        
        # Create a backup of the .bashrc file
        os.system(f'cp {bashrc_path} {backup_path}')
        print(f"Backup of .bashrc created at {backup_path}")
        
        # Check if the line already exists in the file
        with open(bashrc_path, 'r') as file:
            if line.strip() in file.read():
                print("Line already exists in .bashrc")
                return
        
        # Append the line to .bashrc
        with open(bashrc_path, 'a') as file:
            file.write('\n' + line)
            print(f"Added line to .bashrc: {line}")

    except FileNotFoundError as fnf_error:
        print(f"File Error: {fnf_error}")

    except PermissionError:
        print("Permission denied. Run this script with elevated privileges if necessary.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    new_variable = "export MY_VARIABLE='my_value'"
    append_to_bashrc(new_variable)
