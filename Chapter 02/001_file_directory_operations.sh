#!/bin/bash
# Script: File and Directory Operations
# Purpose: Demonstrates basic file and directory operations in Bash.

# List files and directories in the current directory
ls

# List all files and directories, including hidden ones, in detailed format
ls -la

# Change directory to the system's root
cd /

# Go back to the user's home directory
cd ~

# Print the current working directory
pwd

# Create a new directory called 'new_project'
mkdir new_project

# Change to the newly created 'new_project' directory
cd new_project

# Change to the parent directory
cd ..

# Remove an empty directory named 'old_project'
rmdir old_project
