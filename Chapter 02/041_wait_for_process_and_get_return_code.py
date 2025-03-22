# Script: 041_wait_for_process_and_get_return_code.py
# Purpose: Demonstrates how to wait for a process to complete and get its return code using `process.wait()`.

import subprocess

# Start a subprocess (for demonstration, we're running a simple command)
process = subprocess.Popen(["ls", "-l"])

# Wait for the process to complete and get the return code
return_code = process.wait()

# Print the return code of the process
print(f"Process completed with return code {return_code}")
