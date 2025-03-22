# Script: Copy File
# Purpose: Demonstrates how to copy a file from one location to another using Python.

import shutil

# Copy a file from source to destination
# Replace 'source_file' with the path of the file to copy
# Replace 'destination_file' with the path where the file should be copied
shutil.copy('source_file', 'destination_file')

# Print a confirmation message
print("File copied successfully from 'source_file' to 'destination_file'")
