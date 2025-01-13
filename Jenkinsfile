pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'devcodelearn/python-flask-application-using-jenkins'
    }

    stages {
        stage('Clone Repository') {
            steps {
                withCredentials([string(credentialsId: 'github_pat_text', variable: 'GITHUB_PAT')]) {
                    git branch: 'main',
                        url: "https://${GITHUB_PAT}@github.com/devcodelearn/Python-Flask-application-using-Jenkins.git"
                    //try
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Add local bin directory to PATH
                withEnv(['PATH+LOCAL_BIN=/var/lib/jenkins/.local/bin']) {
                    sh 'pytest --maxfail=1 --disable-warnings'
                }
            }
        }

        stage('Dockerize the App') {
            steps {
                script {
                    // Build Docker image
                    //dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}")
                    dockerImage = docker.build('devcodelearn/python-flask-application-using-jenkins')
                    // sh 'sudo docker build -t devcodelearn/python-flask-application-using-jenkins .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Use Jenkins credentials to log in to DockerHub
                    withCredentials([usernamePassword(credentialsId: 'docker_pat', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_TOKEN')]) {
                        // Log in to DockerHub using username and secret token (key)
                        sh "echo $DOCKER_TOKEN | docker login -u $DOCKER_USER --password-stdin"
                        
                        // Push the Docker image to DockerHub
                        dockerImage.push("${env.BUILD_ID}")
                        dockerImage.push("latest")
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Deploy the application as a Docker container
                    sh """
                    docker stop python-flask-application-using-Jenkins || true && docker rm python-flask-application-using-Jenkins || true
                    docker run -d -p 5000:5000 --name python-flask-application-using-jenkins ${DOCKER_IMAGE_NAME}:latest
                    """
                    //docker run -d -p 5000:5000 --name python-flask-application-using-jenkins devcodelearn/python-flask-application-using-jenkins:latest
                    

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
