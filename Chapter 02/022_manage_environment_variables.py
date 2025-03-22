# Script: Manage Environment Variables
# Purpose: Demonstrates how to get and set environment variables using Python.

import os

# Get an environment variable
# Replace 'PATH' with the name of the environment variable you want to retrieve
path = os.environ.get('PATH')
print("Current PATH environment variable:")
print(path)

# Set a new environment variable
# Replace 'MY_VAR' and 'value' with your variable name and desired value
os.environ['MY_VAR'] = 'value'
print("\nEnvironment variable 'MY_VAR' set to:")
print(os.environ['MY_VAR'])
