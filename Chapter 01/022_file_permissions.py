# Import the `os` module for file system operations
import os

# Specify the filename to modify permissions
filename = "example.txt"

# Check if the file exists before modifying permissions
if os.path.exists(filename):
    # Make the file read-only (Linux-based systems)
    os.chmod(filename, 0o444)
    print(f"{filename} is now read-only.")

    # Change the file permissions to give full permissions to the owner (Linux-based systems)
    os.chmod(filename, 0o700)
    print(f"Full permissions have been granted to the owner for {filename}.")
else:
    # Print a message if the file does not exist
    print(f"{filename} does not exist!")
