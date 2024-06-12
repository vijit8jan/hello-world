pipeline {
    agent any
    environment {
        // Define environment variables
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        EC2_IP = 'YOUR_EC2_INSTANCE_PUBLIC_IP'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git 'https://github.com/your-repo/hello-world-python.git'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // SSH into EC2 instance and deploy the application
                    sh '''
                    ssh -o StrictHostKeyChecking=no ec2-user@${EC2_IP} << EOF
                    sudo yum update -y
                    sudo yum install -y python3 git
                    git clone https://github.com/your-repo/hello-world-python.git
                    cd hello-world-python
                    python3 app.py &
                    exit
                    EOF
                    '''
                }
            }
        }
    }
}
