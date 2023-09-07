pipeline {
  agent any
  stages {
    stage('Vagrant') {
      steps {
        script {
            // Run your Vagrant commands here
            sh '''
              echo Vagrant Stage
              uname -a
              echo $PATH
              pwd
              python3 --version
              terraform --version
              '''
              //vagrant up
              //vagrant --version
              // Additional Vagrant commands can be added here
        }
      }
    }
    
    stage ("Gradle Build") {
        steps {
            sh './gradlew clean build'
        }
    }   
  }
}
