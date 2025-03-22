# Script: 011_create_user.py

import subprocess

def create_user(username):
    """
    Creates a new system user if the user does not already exist.
    :param username: The name of the user to create.
    """
    try:
        # Check if the user already exists
        subprocess.run(['id', username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"User '{username}' already exists.")
    except subprocess.CalledProcessError:
        # User does not exist, proceed to create
        try:
            subprocess.run(['sudo', 'useradd', '-m', username], check=True)
            print(f"User '{username}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create user '{username}': {e.stderr.decode().strip()}")
        except PermissionError:
            print("Permission denied. Run this script with elevated privileges.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    username_to_create = 'newuser'  # Replace with the desired username
    create_user(username_to_create)
