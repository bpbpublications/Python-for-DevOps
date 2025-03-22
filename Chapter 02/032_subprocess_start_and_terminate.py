# Script: 032_subprocess_start_and_terminate.py
# Purpose: Demonstrates how to start and terminate a subprocess using the `subprocess` module.

import subprocess

# Starting a new process
# Replace 'your_script.py' with the path to the Python script or command you want to execute
print("Starting the process...")
process = subprocess.Popen(['python', 'your_script.py'])

# Perform other tasks here if needed (simulate with a short delay or logic)

# Terminating the process
print("Terminating the process...")
process.terminate()

# Optional: Wait for the process to terminate (cleanup)
process.wait()
print("Process terminated.")
