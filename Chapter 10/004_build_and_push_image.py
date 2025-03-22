# Script: 004_build_and_push_image.py

def build_and_push_image():
    """
    Builds a Docker image and pushes it to Docker Hub.
    Assumes that Docker is installed and running, and credentials
    for Docker Hub are available in the Jenkins environment.
    """
    
    # Build Docker image
    sh 'docker build -t myapp:latest .'

    # Login to Docker Hub using stored credentials
    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]):
        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"

    # Push Docker image to Docker Hub
    sh 'docker push myapp:latest'

# Example usage (this would typically be executed in a CI/CD pipeline)
build_and_push_image()
