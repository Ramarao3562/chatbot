pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main', url: 'https://github.com/Ramarao3562/note_app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    bat 'python3 -m venv venv'
                    // Activate the virtual environment and install dependencies
                    bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Build Application') {
            steps {
                // Run your application build command if needed
                echo 'Building the application...'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Add your deployment commands here
                    echo 'Deploying the application...'
                    // Example: Move files, restart services, etc.
                }
            }
        }
    }
    post {
        always {
            // Clean up the workspace after the build
            cleanWs()
        }
    }
}
