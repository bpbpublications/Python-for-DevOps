# Script: Run Command and Write Output to File
# Purpose: Demonstrates how to execute a command using the `subprocess` module and write the output to a file.

import subprocess

# Define the command to execute
command = ['ls', '-l']  # Replace this with the actual command you want to run

# Specify the output file
output_file_path = 'output.txt'

try:
    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # Execute the command and redirect the output to the file
        subprocess.run(
            command,
            text=True,  # Ensures the output is written as text
            stdout=output_file,  # Redirects stdout to the file
            stderr=subprocess.PIPE,  # Captures errors in stderr
            check=True  # Raises an exception if the command fails
        )
    print(f"Command executed successfully. Output written to '{output_file_path}'.")
except subprocess.CalledProcessError as e:
    print(f"Error: Command failed with return code {e.returncode}.")
    print(f"Stderr: {e.stderr}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
