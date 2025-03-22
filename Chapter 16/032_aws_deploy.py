# Script: 032_aws_deploy.py

import subprocess

def aws_deploy():
    print("Deploying application to AWS...")
    try:
        # Sync files to S3
        subprocess.run(['aws', 's3', 'sync', './dist', 's3://my-app-bucket'], check=True)

        # Update ECS service
        subprocess.run(['aws', 'ecs', 'update-service', 
                        '--cluster', 'my-cluster', 
                        '--service', 'my-service', 
                        '--force-new-deployment'], check=True)

        print("Deployment successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")

if __name__ == "__main__":
    aws_deploy()
