# Script: 016_deploy_to_elastic_beanstalk.py

import boto3

def deploy_to_elastic_beanstalk(application_name, environment_name, version_label, s3_bucket, s3_key):
    """
    Deploys an application version to AWS Elastic Beanstalk.
    
    :param application_name: The name of the Elastic Beanstalk application.
    :param environment_name: The environment name where the application will be deployed.
    :param version_label: The version label for the application version.
    :param s3_bucket: The S3 bucket where the application source bundle is stored.
    :param s3_key: The S3 key for the application source bundle.
    """
    eb_client = boto3.client('elasticbeanstalk')

    print("Uploading application version...")
    # Create a new application version in Elastic Beanstalk using the source bundle in S3
    eb_client.create_application_version(
        ApplicationName=application_name,
        VersionLabel=version_label,
        SourceBundle={
            'S3Bucket': s3_bucket,
            'S3Key': s3_key
        }
    )

    print("Updating environment...")
    # Update the Elastic Beanstalk environment with the new version
    eb_client.update_environment(
        ApplicationName=application_name,
        EnvironmentName=environment_name,
        VersionLabel=version_label
    )

    print(f"Deployment of {application_name} to {environment_name} completed.")

if __name__ == "__main__":
    # Example: Deploy the Django application to Elastic Beanstalk
    deploy_to_elastic_beanstalk(
        application_name="MyDjangoApp",           # Elastic Beanstalk application name
        environment_name="MyDjangoEnv",           # Environment name for deployment
        version_label="v1.0.0",                   # Version label for this deployment
        s3_bucket="my-eb-deployment-bucket",      # S3 bucket containing the application source
        s3_key="django-backend.zip"               # S3 key for the application source bundle
    )
