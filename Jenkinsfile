pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'pip3 install -r requirements.txt' 
            }
        }
        stage('Test') { 
            steps {
                sh 'python3 nwe_file.py' 
            }
        }

        stage('Deploy-To-Staging') { 
            steps {
                sh 'echo "Deploying to staging "'
                // sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.56.105 "source venv/bin/activate; \
                // cd polling; \
                // git pull origin master; \
                // pip install -r requirements.txt --no-warn-script-location; \
                // python manage.py migrate; \
                // deactivate; \
                // sudo systemctl restart nginx; \
                // sudo systemctl restart gunicorn "' 
            }
        }

    
    }
}
