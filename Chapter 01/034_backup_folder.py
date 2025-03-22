import shutil
import os

def backup_folder(src, dst):
    """
    Creates a backup of the source folder at the destination folder.
    """
    try:
        # Check if the source folder exists
        if not os.path.exists(src) or not os.path.isdir(src):
            print(f"Source folder '{src}' does not exist or is not a valid directory.")
            return
        
        # Check if the destination folder already exists
        if os.path.exists(dst):
            print(f"Destination folder '{dst}' already exists. Choose a different backup location.")
            return
        
        # Copy the entire folder
        shutil.copytree(src, dst)
        print(f"Backup of '{src}' successfully created at '{dst}'.")
    except Exception as e:
        # Handle any exceptions during the backup process
        print(f"An error occurred during backup: {e}")

# Prompt the user for source and destination folder paths
source_folder = input("Enter source folder path: ")
backup_folder_path = input("Enter backup folder path: ")

# Call the function to create the backup
backup_folder(source_folder, backup_folder_path)
