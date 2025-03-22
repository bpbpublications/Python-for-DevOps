# Import the `os` module for file system operations
import os

# Specify the name of the new directory
directory_name = "new_directory"

# Check if the directory already exists
if not os.path.exists(directory_name):
    # Create the directory
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' has been created.")
else:
    # Print a message if the directory already exists
    print(f"Directory '{directory_name}' already exists.")
