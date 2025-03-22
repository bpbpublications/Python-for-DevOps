#!/bin/bash
# Script: File Permission Operations
# Purpose: Demonstrates various `chmod` operations for managing file permissions.

# Add execute permission to the user (owner) of the file
chmod u+x file.py

# Remove read and write permissions from the group and others
chmod go-rw file.py

# Set the permissions:
# Owner: full permissions (read, write, execute)
# Group: read and execute permissions
# Others: no permissions
chmod u=rwx,g=rx,o= file.py

# Add read permission to everyone (user, group, and others)
chmod a+r file.py

# Remove execute permissions from everyone (user, group, and others)
chmod a-x file.py

# Add write permission to the group and others
chmod go+w file.py
