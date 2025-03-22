import os
import shutil

def organize_files(folder_path):
    """
    Organizes files in the given folder into subdirectories based on file extensions.
    """
    # Mapping file extensions to target folder names
    extensions_folders = {
        '.txt': 'TextFiles',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.pdf': 'Documents',
        # Add more extensions and folders as needed
    }

    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Determine the target directory based on the extension
        directory = extensions_folders.get(file_extension)
        if directory:
            # Create the target directory if it doesn't exist
            target_directory = os.path.join(folder_path, directory)
            if not os.path.exists(target_directory):
                os.mkdir(target_directory)
            # Move the file to the appropriate directory
            shutil.move(
                os.path.join(folder_path, filename),
                os.path.join(target_directory, filename)
            )

# Prompt the user for the folder path
folder_path = input("Enter folder path: ")

# Check if the folder exists before organizing files
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    organize_files(folder_path)
    print(f"Files in '{folder_path}' have been organized.")
else:
    print(f"The folder '{folder_path}' does not exist.")
