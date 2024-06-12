pipeline {
    agent any

    environment {
        // Define environment variables
        AWS_REGION = 'us-east-1' // Change to your AWS region
        EC2_INSTANCE_ID = 'i-0123456789abcdef0' // Replace with your EC2 instance ID
        EC2_USER = 'ec2-user'
        SSH_KEY_PATH = '/path/to/your-key-pair.pem' // Replace with the path to your SSH key
        REPO_URL = 'https://github.com/your-repo/hello_world_app.git' // Replace with your repository URL
    }

    stages {
        stage('Provision EC2') {
            steps {
                script {
                    // Add steps to provision EC2 if needed
                    echo 'Provisioning EC2 instance...'
                    // Placeholder for EC2 provisioning script if not already done
                }
            }
        }

        stage('Clone Repository') {
            steps {
                git url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sshagent(['your-ssh-credentials-id']) { // Replace with your Jenkins SSH credentials ID
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} ${EC2_USER}@${EC2_INSTANCE_ID} << EOF
                        sudo yum update -y
                        sudo yum install -y git python3 python3-venv
                        git clone ${REPO_URL}
                        cd hello_world_app
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        EOF
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                sshagent(['your-ssh-credentials-id']) { // Replace with your Jenkins SSH credentials ID
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} ${EC2_USER}@${EC2_INSTANCE_ID} << EOF
                        cd hello_world_app
                        cat <<EOT > /etc/systemd/system/hello_world_app.service
                        [Unit]
                        Description=Hello World Python Application
                        After=network.target

                        [Service]
                        User=ec2-user
                        WorkingDirectory=/home/ec2-user/hello_world_app
                        ExecStart=/home/ec2-user/hello_world_app/venv/bin/python /home/ec2-user/hello_world_app/hello_world/main.py
                        Restart=always

                        [Install]
                        WantedBy=multi-user.target
                        EOT

                        sudo systemctl daemon-reload
                        sudo systemctl start hello_world_app
                        sudo systemctl enable hello_world_app
                        EOF
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sshagent(['your-ssh-credentials-id']) { // Replace with your Jenkins SSH credentials ID
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} ${EC2_USER}@${EC2_INSTANCE_ID} << EOF
                        curl -f http://localhost:80 || exit 1
                        EOF
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
