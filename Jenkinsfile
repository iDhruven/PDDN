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
              '''
              //vagrant up
             // Additional Vagrant commands can be added here
        }
      }
    }
  }
}
