# Import the `os` module for file system operations
import os

# Specify the directory name to change into
directory_name = "new_directory"

# Check if the directory exists
if os.path.exists(directory_name):
    # Change to the specified directory
    os.chdir(directory_name)
    print(f"Changed to the directory: {directory_name}")
else:
    # Print a message if the directory does not exist
    print(f"The directory '{directory_name}' does not exist!")
