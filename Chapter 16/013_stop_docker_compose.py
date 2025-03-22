# Script: 013_stop_docker_compose.py

import subprocess

def stop_docker_compose():
    """
    Stops all running Docker Compose services and removes containers, networks, and volumes.
    """
    print("Stopping Docker Compose...")
    try:
        subprocess.run(["docker-compose", "down"], check=True)  # Stop and clean up Docker Compose
        print("Docker Compose stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping Docker Compose: {e}")

if __name__ == "__main__":
    stop_docker_compose()
