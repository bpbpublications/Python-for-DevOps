# Script: 003_deploy.py

import subprocess

def deploy(environment):
    """
    Deploys the application to the specified environment using kubectl.
    :param environment: The environment to deploy to ('staging' or 'production').
    """
    
    if environment == 'staging':
        # Deploy to staging environment
        subprocess.run(['kubectl', 'apply', '-f', 'staging.yaml'], check=True)
    elif environment == 'production':
        # Deploy to production environment
        subprocess.run(['kubectl', 'apply', '-f', 'production.yaml'], check=True)
    else:
        print(f'Invalid environment: {environment}')

# Example usage: Deploying to 'staging'
deploy('staging')
