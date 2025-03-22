# Script: 015_build_docker_image.py

import subprocess

def build_docker_image(service_name, dockerfile_path):
    """
    Builds a Docker image for a specified service using the provided Dockerfile.

    :param service_name: The name of the service to be used as the image tag.
    :param dockerfile_path: The path to the Dockerfile for building the image.
    """
    print(f"Building Docker image for {service_name}...")
    
    try:
        # Run the Docker build command to create the image
        subprocess.run(
            ["docker", "build", "-t", f"{service_name}:latest", "-f", dockerfile_path, "."],
            check=True
        )
        print(f"Docker image for {service_name} built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")

if __name__ == "__main__":
    # Example: Build the Docker image for the 'django-backend' service using its Dockerfile
    build_docker_image("django-backend", "./Dockerfile")
