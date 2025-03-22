# Script: Execute and Capture Shell Commands
# Purpose: Demonstrates how to execute shell commands and capture their output using the `subprocess` module.

import subprocess

# Run a Bash command and display its output
print("Running 'ls -l' command:")
subprocess.run(['ls', '-l'])  # Replace with any command you want to execute

# Run a Bash command and capture its output
try:
    print("\nCapturing output of 'cat /etc/passwd':")
    result = subprocess.run(
        ['cat', '/etc/passwd'], 
        capture_output=True, 
        text=True, 
        check=True  # Raises an exception if the command fails
    )
    print("Command Output:")
    print(result.stdout)  # Print the captured output
except subprocess.CalledProcessError as e:
    print(f"Error: Command failed with return code {e.returncode}.")
    print(f"Stderr: {e.stderr}")
except FileNotFoundError:
    print("Error: The specified file does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
