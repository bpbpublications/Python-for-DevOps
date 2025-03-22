# Script: 020_backup_files.py

import shutil
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='backup.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def backup_files(source, destination):
    """
    Backs up files and directories from a source to a destination.
    
    Parameters:
        source (str): Path to the source directory.
        destination (str): Path to the destination directory.
    """
    try:
        # Ensure the source directory exists
        if not os.path.exists(source):
            logging.error(f"Source directory {source} does not exist.")
            return

        # Ensure the destination directory exists, if not, create it
        if not os.path.exists(destination):
            os.makedirs(destination)

        # List all files and directories in the source
        items = os.listdir(source)

        # Copy each item to the destination
        for item in items:
            src_path = os.path.join(source, item)
            dest_path = os.path.join(destination, item)
            if os.path.isdir(src_path):
                # Copy entire directory
                shutil.copytree(src_path, dest_path)
            else:
                # Copy file
                shutil.copy2(src_path, dest_path)
            
            logging.info(f"Copied {src_path} to {dest_path}")

        logging.info("Backup completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    source_dir = '/path/to/source'  # Replace with the actual source directory path
    destination_dir = f'/path/to/destination/backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'  # Timestamped backup
    backup_files(source_dir, destination_dir)
