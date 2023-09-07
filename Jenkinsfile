pipeline {
    environment{
        image_name = dhruven_springboot+mysql
        docker_image = ''
    }

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
                    '''
                    //vagrant up
                    //vagrant --version
                    // Additional Vagrant commands can be added here
                }
            }
        }

        stage ("Gradle Build") {
            steps {
            sh '''
                python3 gradlew.py
            '''
            }
        }
        
        stage ("Building/Dockerizing Image") {
            steps {
                script {
                    dockerImage = docker.build("${env.image_name}", ".")
                }
            }
        }
        
    }
}
