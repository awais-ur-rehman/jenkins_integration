pipeline {
    agent any

    environment {
        NODE_HOME = '/usr/bin'
        SELENIUM_VENV = '.venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/<your-username>/jenkins_integration.git'
            }
        }

        stage('Install Node.js Dependencies') {
            steps {
                script {
                    sh 'npm install'
                }
            }
        }

        stage('Start Node.js Server') {
            steps {
                script {
                    sh 'nohup npm start &'
                }
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv ${SELENIUM_VENV}'
                    sh 'source ${SELENIUM_VENV}/bin/activate && pip install selenium'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    sh 'source ${SELENIUM_VENV}/bin/activate && python selenium_tests.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                sh 'pkill -f node || true'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
