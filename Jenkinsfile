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
              chmod +x Vagrant.sh
              ./Vagrant.sh
              echo $PATH
              pwd
              python3 --version
              /Users/idhruven/.jenkins/workspace/PDDN/vagrant --version
              '''
              //vagrant up
              //vagrant --version
              // Additional Vagrant commands can be added here
        }
      }
    }
  }
}
