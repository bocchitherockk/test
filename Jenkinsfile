pipeline {
    agent any

    stages {

        // Checkout the code from the repository
        // This is a redundant step as Jenkins automatically checks out the code by default, but it's included here for clarity.
        // stage('Checkout') {
        //     steps {
        //         checkout scm
        //     }
        // }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    pip install -r requirements-dev.txt
                    pip install -e .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest tests
                '''
            }
        }
    }
}