# Import the `os` module for file system operations
import os

# Specify the directory name to delete
directory_name = "new_directory"

# Check if the directory exists
if os.path.exists(directory_name):
    # Remove the directory
    os.rmdir(directory_name)
    print(f"Directory '{directory_name}' has been deleted.")
else:
    # Print a message if the directory does not exist
    print(f"The directory '{directory_name}' does not exist!")
