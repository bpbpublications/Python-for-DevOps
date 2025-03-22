# Import the `os` module for file system operations and `time` module for time formatting
import os
import time

# Specify the filename to check
filename = "example.txt"

# Check if the file exists before attempting to get its modification time
if os.path.exists(filename):
    # Get the last modification time of the file in seconds since the epoch
    modification_time = os.path.getmtime(filename)
    # Convert the modification time into a readable string format
    readable_time = time.ctime(modification_time)
    # Print the last modification time of the file
    print(f"{filename} was last modified on {readable_time}.")
else:
    # Print a message if the file does not exist
    print(f"{filename} does not exist!")
