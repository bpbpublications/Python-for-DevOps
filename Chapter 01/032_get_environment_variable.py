# Import the `os` module to work with environment variables
import os

# Retrieve the environment variable 'SECRET_KEY'
secret_key = os.getenv('SECRET_KEY')

# If the environment variable is not set, provide a default value
secret_key = os.getenv('SECRET_KEY', 'default_value')

# Use the sensitive information securely
print(secret_key)  # Avoid printing sensitive information in production!
