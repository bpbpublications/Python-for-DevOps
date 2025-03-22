# Import the `shutil` module for file operations
import shutil
import os

# Specify the source file and destination path
source = "example.txt"
destination = "new_folder/example.txt"

# Check if the source file exists before attempting to move it
if os.path.exists(source):
    # Move the file to the new location
    shutil.move(source, destination)
    # Print confirmation of the move
    print(f"Moved {source} to {destination}.")
else:
    # Print a message if the source file does not exist
    print(f"{source} does not exist!")
