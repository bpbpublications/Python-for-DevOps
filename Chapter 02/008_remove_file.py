# Script: Remove File
# Purpose: Demonstrates how to delete a file using Python.

import os

# Remove a file at the specified path
# Replace '/path/to/file' with the actual path of the file to delete
try:
    os.remove('/path/to/file')
    print("File deleted successfully: /path/to/file")
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied. Unable to delete the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
