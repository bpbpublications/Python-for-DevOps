# Script: 039_check_process_status.py
# Purpose: Demonstrates how to check the status of a running process using `process.poll()`.

import subprocess

# Start a subprocess (for demonstration purposes, we're running a simple command)
process = subprocess.Popen(['sleep', '5'])  # Sleep for 5 seconds

# Check the process status using poll
return_code = process.poll()

if return_code is None:
    # If poll returns None, the process is still running
    print("Process is still running")
else:
    # If poll returns a return code, the process has finished
    print(f"Process finished with return code {return_code}")
