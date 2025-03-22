# Script: 024_run_subprocess_commands.py
# Purpose: Demonstrates how to run shell commands using the `subprocess` module and capture output.

import subprocess

# Run a simple shell command
# The 'ls -l' command lists files and directories in long format
print("Running 'ls -l':")
subprocess.run(["ls", "-l"])

# Run a shell command and capture its output
# The 'echo' command prints a string to the terminal
print("\nCapturing output of 'echo Hello World':")
result = subprocess.run(["echo", "Hello World"], capture_output=True, text=True)

# Print the captured output
print("Captured Output:")
print(result.stdout)
