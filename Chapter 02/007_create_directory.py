# Script: Create Directory
# Purpose: Demonstrates how to create a directory (and any necessary parent directories) using Python.

import os

# Create a directory, including any necessary parent directories
# Replace '/path/to/new_directory' with the actual path of the directory to create
# `exist_ok=True` ensures no error is raised if the directory already exists
os.makedirs('/path/to/new_directory', exist_ok=True)

# Print a confirmation message
print("Directory created (or already exists): /path/to/new_directory")
