#!/bin/bash
# Script: Bash and Python Piping
# Purpose: Demonstrates how to pipe output between Bash commands and Python scripts.

# Piping Bash command output to a Python script
# Replace '/path/to/receive_input.py' with the actual path to your Python script
echo "data" | python3 receive_input.py

# Piping Python script output to a Bash command
# Replace '/path/to/generate_output.py' with the actual path to your Python script
# Replace 'pattern' with the string or pattern you want to search for
python3 generate_output.py | grep 'line'
