# Import the `os` module for file system operations
import os

# Specify the filename to check
filename = "example.txt"

# Check if the file exists
if os.path.exists(filename):
    # Print a message if the file exists
    print(f"{filename} exists!")
else:
    # Print a message if the file does not exist
    print(f"{filename} does not exist!")
