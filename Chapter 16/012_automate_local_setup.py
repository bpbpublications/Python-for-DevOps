# Script: 012_automate_local_setup.py

import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from a .env file
def load_env():
    """
    Loads environment variables from a .env file if it exists.
    """
    print("Loading environment variables...")
    if os.path.exists(".env"):
        load_dotenv()
        print("Environment variables loaded successfully.")
    else:
        print(".env file not found. Please create it with the necessary variables.")

# Start Docker Compose to build and run services
def start_docker_compose():
    """
    Starts Docker Compose with the build process.
    """
    print("Starting Docker Compose...")
    try:
        subprocess.run(["docker-compose", "up", "--build"], check=True)
        print("Docker Compose started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting Docker Compose: {e}")

# Initialize services, such as setting up databases
def initialize_services():
    """
    Runs initialization tasks for local services, such as database migrations.
    """
    print("Initializing local services...")
    try:
        # Run database migrations for website-backend and blog-backend services
        subprocess.run(["docker-compose", "exec", "website-backend", "python", "manage.py", "migrate"], check=True)
        subprocess.run(["docker-compose", "exec", "blog-backend", "python", "manage.py", "migrate"], check=True)
        print("Services initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing services: {e}")

if __name__ == "__main__":
    print("Automating local environment setup...")
    load_env()  # Load environment variables
    start_docker_compose()  # Start Docker Compose
    initialize_services()  # Initialize services
    print("Local environment setup completed.")
