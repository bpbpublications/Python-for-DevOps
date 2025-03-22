#!/bin/bash
# Script: File Permission Modes
# Purpose: Demonstrates numeric `chmod` operations to set file permissions.

# Set permissions:
# Owner: full permissions (read, write, execute - 7)
# Group: read and execute permissions (5)
# Others: read permissions only (4)
chmod 754 file.py

# Set permissions:
# Owner: read and write permissions (6)
# Group: read permissions only (4)
# Others: no permissions (0)
chmod 640 file.py

# Give read, write, and execute permissions to everyone
chmod 777 file.py

# Remove all permissions from group and others:
# Owner: full permissions (7)
# Group: no permissions (0)
# Others: no permissions (0)
chmod 700 file.py

# Set permissions:
# Owner: read and execute permissions (5)
# Group: read and execute permissions (5)
# Others: no permissions (0)
chmod 550 file.py

# Set permissions:
# Owner: read, write, and execute permissions (5 + 1 + 5 = 511)
# Group: no permissions (0)
# Others: no permissions (0)
chmod 511 file.py
