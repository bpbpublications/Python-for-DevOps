# Script: List Files in Directory
# Purpose: Demonstrates how to list all files and directories in a specified directory using Python.

import os

# List all files and directories in the specified path
# Replace '/path/to/directory' with the actual path you want to list
files = os.listdir('/path/to/directory')

# Print the list of files and directories
print("Files and directories in the specified path:", files)
