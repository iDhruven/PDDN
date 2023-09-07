pipeline {
    environment{
        image_name = "dhruven/springboot-mysql"
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
                        /usr/local/bin/docker --version
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
                    sh'''
                        /usr/local/bin/docker build -t ${env.image_name} .
                    '''
                    //dockerImage = docker.build("${env.image_name}", ".")
                }
            }
        }
        
    }
}
