pipeline{
    agent any
    stages{
        stage("Checkout"){
            steps{
                git 'https://github.com/cubesrepo/orangeHRM'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv orangeVenv'
                bat 'orangeVenv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'orangeVenv\\Scripts\\activate && pytest -v --html=report.html'
            }
        }
    }
}