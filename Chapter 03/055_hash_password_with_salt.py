# Script: 055_hash_password_with_salt.py

# Importing hashlib and os modules for hashing and generating a salt
import hashlib
import os

# Generating a new salt (32 bytes) for the user
salt = os.urandom(32)

# Encoding the password (this should be done with any input password)
password = 'password123'.encode('utf-8')

# Hashing the password using PBKDF2-HMAC with SHA-256, salt, and 100,000 iterations
hash = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
