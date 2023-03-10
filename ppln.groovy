pipeline {
  agent any
  stages {
    stage('Build and run container') {
      steps {
        withCredentials([string(credentialsId: 'your-credential-id', variable: 'API_KEY')]) 
        {
          sh 'docker run -e API_KEY=$API_KEY your-image-name'
        }
      }
    }
  }
}
