# Script: 012_modify_user.py

import subprocess

def modify_user(username, shell=None, home_dir=None):
    """
    Modifies a system user's settings such as shell or home directory.
    :param username: The name of the user to modify.
    :param shell: The new shell for the user (optional).
    :param home_dir: The new home directory for the user (optional).
    """
    command = ['sudo', 'usermod']
    if shell:
        command += ['-s', shell]
    if home_dir:
        command += ['-d', home_dir]
    command.append(username)
    
    try:
        subprocess.run(command, check=True)
        print(f"User '{username}' modified successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to modify user '{username}': {e.stderr.decode().strip()}")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    username_to_modify = 'newuser'  # Replace with the target username
    shell_to_set = '/bin/bash'  # Replace with the desired shell
    new_home_dir = '/new/home/dir'  # Replace with the desired home directory
    
    modify_user(username_to_modify, shell=shell_to_set, home_dir=new_home_dir)
