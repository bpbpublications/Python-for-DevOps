# Script: 022_build_and_dockerize_react_app.py

import os
import subprocess

def build_react_app(app_directory):
    """
    Builds the React application by installing dependencies and running the build script.

    :param app_directory: The path to the React application directory.
    """
    print("Building React application...")

    # Change to the React app directory
    os.chdir(app_directory)

    try:
        # Install the dependencies using npm
        subprocess.run(["npm", "install"], check=True)

        # Run the build command to create a production build of the React app
        subprocess.run(["npm", "run", "build"], check=True)

        print("React application built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building React application: {e}")

def dockerize_react_app(dockerfile_path, image_name):
    """
    Dockerizes the React application by building a Docker image.

    :param dockerfile_path: The path to the Dockerfile used for building the image.
    :param image_name: The name and tag for the Docker image.
    """
    print("Creating Docker image for React application...")

    try:
        # Build the Docker image using the specified Dockerfile
        subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile_path, "."], check=True)

        print(f"Docker image '{image_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating Docker image: {e}")

if __name__ == "__main__":
    # Example: Build the React app in './my-react-app' and dockerize it using the provided Dockerfile
    build_react_app("./my-react-app")
    dockerize_react_app("./Dockerfile", "my-react-frontend:latest")
