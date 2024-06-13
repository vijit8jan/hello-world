pipeline {
    agent any
    environment {
        // Define environment variables
        //AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
       // AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        SSH_KEY = credentials('ssh_key')
        EC2_IP = '3.92.66.254'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git branch: 'main', url: 'https://github.com/vijit8jan/hello-world.git'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // SSH into EC2 instance and deploy the application
                    sh '''
                    ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ubuntu@${EC2_IP} << EOF
                    sudo apt update -y
                    sudo apt install -y python3 git
                    cd ~
                    git clone https://github.com/rushikeshmj/hello-world.git
                    cd /home/ubuntu/hello-world
                    python3 main.py &
                    exit
                    EOF
                    '''
                }
            }
        }
    }
}
