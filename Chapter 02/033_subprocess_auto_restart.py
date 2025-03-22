# Script: 033_subprocess_auto_restart.py
# Purpose: Demonstrates how to restart a subprocess automatically if it terminates unexpectedly.

import subprocess

while True:
    # Start the subprocess
    print("Starting the process...")
    process = subprocess.Popen(['python', 'your_script.py'])

    # Wait for the process to terminate
    process.wait()

    # Check the process return code
    if process.returncode != 0:
        print("Process terminated unexpectedly. Restarting...")
    else:
        print("Process ended normally. Exiting loop.")
        break  # Exit the loop if the process ends successfully
