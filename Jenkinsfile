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
                        echo $JAVA_HOME
                        pwd
                        python3 --version
                        which java
                        /usr/local/bin/terraform --version
                        /usr/local/bin/docker --version
                        echo "Please Fill the Teraform Variables for the AWS Instances - KubernetesMaster, KubernetesWorkers(1,2), JenkinsServer, NginxServer"
                    '''
                    //vagrant up
                    //java --version
                    //javac --version
                    //vagrant --version
                    // Additional Vagrant commands can be added here
                }
            }
        }

        stage ("Gradle Build") {
            steps {
                script{
                        //cleanWs()
                        // python3 gradlew.py
                        sh '''
                            chmod +x ./gradlew
                            ./gradlew clean build       
                        '''
                }
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


        stage ("Post-Build") {
            steps {
                cleanWs()
            }
        }
    }
}
