pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/awais-ur-rehman/jenkins_integration'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Run Server') {
            steps {
                sh 'node server.js &'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh 'python3 selenium_tests.py'
            }
        }
    }
}