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
              ./Vagrant.sh
              python3 --version
              vagrant --version
              '''
              //vagrant up
              //vagrant --version
              // Additional Vagrant commands can be added here
        }
      }
    }
  }
}
