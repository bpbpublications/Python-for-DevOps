#!/bin/bash

# Script: upload_script.sh
# Purpose: Upload a file to example.com using curl

# Check if the file path argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

FILE_PATH="$1"

# Check if the file exists
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File '$FILE_PATH' does not exist."
    exit 1
fi

# Upload the file using curl
UPLOAD_URL="https://example.com/upload"
echo "Uploading file: $FILE_PATH to $UPLOAD_URL"

response=$(curl -F "file=@$FILE_PATH" "$UPLOAD_URL")

if [ $? -eq 0 ]; then
    echo "File '$FILE_PATH' uploaded successfully! Response: $response"
else
    echo "Error: Failed to upload file."
fi
