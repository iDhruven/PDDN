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
              /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
              brew install vagrant
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
