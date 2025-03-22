# Script: 053_encrypt_decrypt_data.py

# Importing the Fernet class from the cryptography.fernet module for symmetric encryption
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()

# Create a cipher object using the generated key
cipher = Fernet(key)

# Encrypting the data
text = b"Hello, World!"  # The data to be encrypted (must be bytes)
encrypted_text = cipher.encrypt(text)

# Decrypting the data back to its original form
decrypted_text = cipher.decrypt(encrypted_text)
