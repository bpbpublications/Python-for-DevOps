# Script: Search Pattern in File
# Purpose: Demonstrates how to use the `subprocess` module to execute the `grep` command to search for a pattern in a file.

import subprocess

# Define the pattern to search for and the file path
pattern = 'pattern'  # Replace with the actual pattern you want to search for
file_path = '/path/to/file'  # Replace with the path of the file to search

try:
    # Execute the grep command to search for the pattern in the file
    result = subprocess.run(
        ['grep', pattern, file_path],
        text=True,  # Ensures output is returned as a string
        capture_output=True,  # Captures stdout and stderr
        check=True  # Raises an exception if the command fails
    )

    # Print the output of the grep command
    print("Search results:")
    print(result.stdout)
except subprocess.CalledProcessError:
    print(f"Pattern '{pattern}' not found in the file: {file_path}")
except FileNotFoundError:
    print(f"Error: The file does not exist: {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
