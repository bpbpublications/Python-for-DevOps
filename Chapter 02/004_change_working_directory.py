# Script: Change Working Directory
# Purpose: Demonstrates how to change the current working directory using Python.

import os

# Change the current working directory to the specified path
# Replace '/path/to/directory' with the actual path you want to navigate to
os.chdir('/path/to/directory')

# Print the new current working directory to confirm the change
print("Current working directory:", os.getcwd())
