pipeline {
  agent any
  stages {
    stage('Vagrant') {
      steps {
        script {
            // Run your Vagrant commands here
            load 'Vagrant.sh'
            sh '''
              echo Vagrant Stage
              uname -a
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
