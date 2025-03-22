# Import the `os` module for file system operations
import os

# Specify the directory name to list contents
directory_name = "new_directory"

# Check if the directory exists
if os.path.exists(directory_name):
    # List the contents of the directory
    contents = os.listdir(directory_name)
    print(f"Contents of '{directory_name}': {contents}")
else:
    # Print a message if the directory does not exist
    print(f"The directory '{directory_name}' does not exist!")
