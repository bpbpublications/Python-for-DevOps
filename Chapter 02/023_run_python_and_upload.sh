#!/bin/bash
# Script: Run Python Script and Upload Processed File
# Purpose: Invokes a Python script to process a data file, captures the output, and uploads the processed file.

# Define the path to the input data file
input_file="/path/to/input_data.txt"  # Replace with the actual path to your input data file

# Invoke the Python script and capture the output
processed_file=$(python3 process_data.py "$input_file")

# Check if the Python script produced output
if [ -n "$processed_file" ] && [ -f "$processed_file" ]; then
    echo "Python processing complete. File located at: $processed_file"

    # Continue with further processing, e.g., upload the file
    # Replace '/path/to/upload_script.sh' with your actual upload script
    /path/to/upload_script.sh "$processed_file"

    # Check the exit status of the upload script
    if [ $? -eq 0 ]; then
        echo "File uploaded successfully."
    else
        echo "File upload failed."
    fi
else
    echo "Python script did not produce output."
    exit 1  # Exit with an error code
fi
