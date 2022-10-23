pipeline {
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    agent { label "assignment" }
    stages {
        stage("Stop old image") {
            steps {
                sh "\044(docker ps -a -q) || docker stop \044(docker ps -a -q)"
                sh "\044(docker ps -a -q) || docker rm \044(docker ps -a -q)"
            }
        }
        stage('Get git files') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/robertharedev/WileyAssignment.git']]])
            }
        }
        stage('Build docker image') {
            steps {
                sh "docker build -t py-server ."
            }
        }
        stage('Run docker image') {
            steps {
                sh "docker run -d -p 8000:8000 py-server"
            }
        }
        stage('Push docker image to docker hub') {
            steps {
                sh "docker tag py-server:latest rhdev1/c270assignment:latest"
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh "docker push rhdev1/c270assignment:latest"
            }
        }
    }
}
