// Script: 031_jenkins_pipeline.groovy

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python scripts/build.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python scripts/test.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python scripts/deploy_to_aws.py'
            }
        }
    }
}
