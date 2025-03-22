# Script: 014_change_file_permissions_and_ownership.py

import os

def change_permissions(file_path, mode):
    """
    Changes file permissions.
    :param file_path: Path to the file.
    :param mode: New permissions in octal format (e.g., 0o755).
    """
    try:
        os.chmod(file_path, mode)
        print(f"Changed permissions for {file_path} to {oct(mode)}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied. Run this script with elevated privileges to change permissions for {file_path}.")
    except Exception as e:
        print(f"Error changing permissions for {file_path}: {e}")

def change_ownership(file_path, uid, gid):
    """
    Changes file ownership.
    :param file_path: Path to the file.
    :param uid: User ID to set as the owner.
    :param gid: Group ID to set as the group.
    """
    try:
        os.chown(file_path, uid, gid)
        print(f"Changed ownership for {file_path} to UID: {uid}, GID: {gid}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied. Run this script with elevated privileges to change ownership for {file_path}.")
    except Exception as e:
        print(f"Error changing ownership for {file_path}: {e}")

if __name__ == "__main__":
    # Example Usage
    file_path = '/path/to/your/file'  # Replace with the actual file path
    new_mode = 0o755  # Read and execute by everyone, write by owner
    user_id = 1000  # Replace with the actual user ID
    group_id = 1000  # Replace with the actual group ID

    change_permissions(file_path, new_mode)
    change_ownership(file_path, user_id, group_id)
