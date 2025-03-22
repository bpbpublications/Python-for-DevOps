# Script: Disk Usage and System Processes
# Purpose: Demonstrates how to use the `subprocess` module to execute system commands for checking disk usage and system processes.

import subprocess

try:
    # Display disk space usage in human-readable format
    print("Disk Usage Information:")
    subprocess.run(['df', '-h'], check=True)
    
    # Display system processes in batch mode with one iteration
    print("\nSystem Processes (Snapshot):")
    subprocess.run(['top', '-b', '-n', '1'], check=True)

except subprocess.CalledProcessError as e:
    # Handle errors if a command fails
    print(f"An error occurred while executing a command: {e}")
    print(f"Command: {e.cmd}")
    print(f"Return code: {e.returncode}")
except Exception as e:
    # Handle any unexpected errors
    print(f"An unexpected error occurred: {e}")
