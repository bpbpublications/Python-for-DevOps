# Script: 001_generate_pipeline.py

def generate_pipeline(environment):
    """
    Generates a pipeline script for different environments (dev or prod).
    :param environment: The environment for the pipeline ('dev' or 'prod').
    :return: A string containing the pipeline script for the given environment.
    """
    
    if environment == 'dev':
        # Pipeline configuration for 'dev' environment
        pipeline_script = """
            pipeline {
                agent any
                stages {
                    stage('Checkout') {
                        steps {
                            git 'https://github.com/example/project.git'
                        }
                    }
                    stage('Build') {
                        steps {
                            sh 'make build'
                        }
                    }
                    stage('Test') {
                        steps {
                            sh 'make test'
                        }
                    }
                    stage('Deploy') {
                        steps {
                            sh 'make deploy-dev'
                        }
                    }
                }
            }
        """
    elif environment == 'prod':
        # Pipeline configuration for 'prod' environment
        pipeline_script = """
            pipeline {
                agent any
                stages {
                    stage('Checkout') {
                        steps {
                            git 'https://github.com/example/project.git'
                        }
                    }
                    stage('Build') {
                        steps {
                            sh 'make build'
                        }
                    }
                    stage('Test') {
                        steps {
                            sh 'make test'
                        }
                    }
                    stage('Deploy') {
                        steps {
                            sh 'make deploy-prod'
                        }
                    }
                }
            }
        """
    else:
        raise ValueError(f'Invalid environment: {environment}')

    return pipeline_script

# Usage
environment = 'dev'  # Can be 'dev' or 'prod'
pipeline_script = generate_pipeline(environment)
print(pipeline_script)
