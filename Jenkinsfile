pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/pawas1g/ml-ops-09march.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-fastapi-app dataset/'
            }
        }

        stage('Stop old Container') {
            steps {
                sh 'docker stop ml-container || true'
                sh 'docker rm ml-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name ml-container ml-fastapi-app'
            }
        }

    }
}