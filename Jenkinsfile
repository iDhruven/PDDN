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
              brew update python
              python3 --version
              '''
              //vagrant up
              //vagrant --version
              // Additional Vagrant commands can be added here
        }
      }
    }
  }
}
