# Script: 037_fork_process.py
# Purpose: Demonstrates how to use `os.fork()` to create a child process in Unix/Linux systems.

import os

# Get the current process ID
pid = os.getpid()
print("Current PID:", pid)

# Fork a new process (this works only on Unix/Linux systems)
if os.fork() == 0:
    # Child process
    print("In child process")
else:
    # Parent process
    print("In parent process")
