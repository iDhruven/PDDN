pipeline {
    environment{
        image_name = "dhruven/springboot-mysql"
        docker_image = ''
    }

    agent any

    stages {
        stage('Terraform') {
            steps {
                script {
                    // Run your Vagrant commands here
                    sh '''
                        echo Terraform Stage
                        uname -a
                        echo $PATH
                        pwd
                        python3 --version
                        java --version
                        javac --version
                        /usr/local/bin/terraform --version
                        /usr/local/bin/docker --version
                        echo "Please Fill the Teraform Variables for the AWS Instances - KubernetesMaster, KubernetesWorkers(1,2), JenkinsServer, NginxServer"
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
                        /usr/local/bin/docker build -t $image_name .
                    '''
                    //dockerImage = docker.build("${env.image_name}", ".")
                }
            }
        }
        
    }
}
