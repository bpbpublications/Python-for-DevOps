# Script: 002_deploy_to_staging.py

def deploy_to_staging():
    """
    Deploys the application to the staging environment by performing
    the following steps:
    1. Checkout the code from version control.
    2. Build and package the application.
    3. Run tests.
    4. Deploy to the staging environment.
    """
    
    # Checkout code from version control
    git 'https://github.com/example/project.git'

    # Build and package the application
    sh 'make build'

    # Run tests
    sh 'make test'

    # Deploy to staging environment
    sh 'python deploy.py staging'

# Example usage (call the function to initiate deployment)
deploy_to_staging()
