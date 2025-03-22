# Script: Execute Multiple Commands Sequentially
# Purpose: Demonstrates how to execute multiple commands using the `subprocess` module and handle errors.

import subprocess

try:
    # Execute the first command
    subprocess.run(['ls'], check=True)
    print("Command `ls` executed successfully.")
    
    # Execute the second command
    subprocess.run(['pwd'], check=True)
    print("Command `pwd` executed successfully.")

except subprocess.CalledProcessError as e:
    # Handle errors if a command fails
    print(f"An error occurred while executing a command: {e}")
    print(f"Command: {e.cmd}")
    print(f"Return code: {e.returncode}")
except Exception as e:
    # Handle any unexpected errors
    print(f"An unexpected error occurred: {e}")
