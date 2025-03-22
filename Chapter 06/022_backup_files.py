# Script: 022_backup_files.py

import shutil
import os
from datetime import datetime

def backup_files(source, destination):
    """
    Creates a timestamped backup of a file or directory.
    :param source: Path to the source file or directory to back up.
    :param destination: Path to the destination directory where the backup will be stored.
    """
    try:
        # Create a timestamped backup folder
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        backup_folder = os.path.join(destination, f'backup-{timestamp}')
        os.makedirs(backup_folder, exist_ok=True)

        # Copy files or directories
        if os.path.isdir(source):
            shutil.copytree(source, os.path.join(backup_folder, os.path.basename(source)))
        else:
            shutil.copy2(source, backup_folder)

        print(f"Backup of {source} completed. Backup stored in {backup_folder}")
    except FileNotFoundError:
        print(f"Source path not found: {source}")
    except PermissionError:
        print(f"Permission denied. Run this script with elevated privileges for {destination}.")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    # Example usage
    source_path = '/path/to/source/file_or_directory'  # Replace with the actual source path
    destination_path = '/path/to/backup/destination'  # Replace with the actual destination path
    
    backup_files(source_path, destination_path)
