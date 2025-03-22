#!/bin/bash
# Script: Embed Python in Bash
# Purpose: Demonstrates how to embed Python code directly within a Bash script.

# Embedding Python in a Bash script
python3 << END
import sys

# Print a message from Python
print('Hello from Python!')

# Exit the script with a success code
sys.exit(0)
END