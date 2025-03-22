# Script: 040_subprocess_capture_output_and_error.py
# Purpose: Demonstrates how to run a subprocess, capture both standard output and error, and handle them.

import subprocess

# Start the subprocess and capture both stdout and stderr
process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Communicate with the process to get the output and errors (if any)
stdout, stderr = process.communicate()

# Print the standard output (stdout)
print("Output:", stdout.decode())

# If there was an error, print the standard error (stderr)
if stderr:
    print("Error:", stderr.decode())
