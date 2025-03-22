# Script: 013_delete_user.py

import subprocess

def delete_user(username):
    """
    Deletes a system user along with their home directory and files.
    :param username: The name of the user to delete.
    """
    try:
        subprocess.run(['sudo', 'userdel', '-r', username], check=True)
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete user '{username}': {e.stderr.decode().strip()}")
    except PermissionError:
        print("Permission denied. Run this script with elevated privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    username_to_delete = 'newuser'  # Replace with the target username
    delete_user(username_to_delete)
