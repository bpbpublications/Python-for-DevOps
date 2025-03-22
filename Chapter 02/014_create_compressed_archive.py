# Script: Create a Compressed Archive
# Purpose: Demonstrates how to create a compressed archive (e.g., .tar.gz) of a directory using the `shutil` module.

import shutil

# Define the archive name, format, and source directory
archive_name = 'archive'  # Name of the output archive (without extension)
archive_format = 'gztar'  # Compression format ('gztar' for .tar.gz)
source_directory = '/path/to/directory'  # Replace with the directory to archive

try:
    # Create the compressed archive
    shutil.make_archive(archive_name, archive_format, source_directory)
    print(f"Archive created successfully: {archive_name}.tar.gz")
except FileNotFoundError:
    print(f"Error: The directory '{source_directory}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
