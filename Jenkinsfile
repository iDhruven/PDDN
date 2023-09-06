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
            
              brew install vagrant
              python3 --version
              vagrant --version
              '''
              ///bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
              //vagrant up
              //vagrant --version
              // Additional Vagrant commands can be added here
        }
      }
    }
  }
}
