# Script: 038_subprocess_run_capture_output.py
# Purpose: Demonstrates how to run a shell command using `subprocess.run()` and capture its output.

import subprocess

# Run the shell command 'ls -l' and capture the output
completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Print the captured output from the command
print("Output:", completed.stdout)
