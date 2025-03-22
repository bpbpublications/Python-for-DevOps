# Import the `os` module for file system operations
import os

# Specify the filename to check
filename = "example.txt"

# Check if the file exists before attempting to get its size
if os.path.exists(filename):
    # Get the size of the file in bytes
    file_size = os.path.getsize(filename)
    # Print the size of the file
    print(f"The size of {filename} is {file_size} bytes.")
else:
    # Print a message if the file does not exist
    print(f"{filename} does not exist!")
