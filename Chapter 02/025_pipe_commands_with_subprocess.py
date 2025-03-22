# Script: 025_pipe_commands_with_subprocess.py
# Purpose: Demonstrates how to pipe shell commands using the `subprocess` module in Python.

import subprocess

# Piping commands
try:
    # Start the `grep` process to search for the string "python"
    grep_process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True  # Ensures the data is treated as text
    )

    # Start the `ls` process and pipe its output to the `grep` process
    ls_process = subprocess.Popen(
        ["ls"],
        stdout=grep_process.stdin,
        text=True  # Ensures the data is treated as text
    )

    # Wait for the `ls` process to complete
    ls_process.wait()

    # Get the output from the `grep` process
    output, _ = grep_process.communicate()

    # Print the results
    print("Piped Output:")
    print(output)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
