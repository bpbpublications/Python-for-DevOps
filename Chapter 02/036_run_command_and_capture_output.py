# Script: 036_run_command_and_capture_output.py
# Purpose: Demonstrates how to run a shell command and capture its output using `subprocess.run`.

import subprocess

# Run a shell command and capture its output
# The command 'ls -l' lists files and directories in the current directory in long format
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print the captured output
print("Output:", result.stdout)
