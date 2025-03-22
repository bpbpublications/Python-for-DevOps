# Script: 014_setup_django_environment.py

import os
from dotenv import load_dotenv

def setup_django_environment():
    """
    Sets up the Django environment by loading environment variables from a .env file 
    and setting essential environment variables for Django settings and services.
    """
    print("Setting up Django environment...")

    # Check if the .env file exists and load environment variables
    if os.path.exists(".env"):
        load_dotenv()  # Load variables from .env into the environment
        print("Environment variables loaded successfully.")
    else:
        print(".env file not found. Create it with the necessary configurations.")

    # Set environment variables for Django settings and services
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # Set the Django settings module
    os.environ.setdefault("DATABASE_URL", "postgres://user:password@localhost:5432/website_db")  # Database URL
    os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")  # Redis URL
    print("Environment setup complete.")

if __name__ == "__main__":
    setup_django_environment()
