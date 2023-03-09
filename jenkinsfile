pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '/path/to/python -m pytest'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker build -t myapp .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                }
                sh 'docker tag myapp myuser/myapp:latest'
                sh 'docker push myuser/myapp:latest'
            }
        }
    }
}
