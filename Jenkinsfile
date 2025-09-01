pipeline {
    agent any

    environment {
        REGISTRY     = '172.17.0.3:5000'           // IP of the local Docker registry
        IMAGE_NAME   = 'my-flask-app'
        TAG          = "V-${BUILD_NUMBER}"
        HOST_PORT    = "1234"
        CONT_PORT    = "5000"
        CONT_NAME    = "flask-app"
        REPO_NAME    = "${IMAGE_NAME}"
    }

    stages {

        stage('Clear Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sayantan2k24/flask-app-for-jenkins-docker-self-hosted-registry.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${REGISTRY}/${IMAGE_NAME}:${TAG} ."
                }
            }
        }

        stage('Push to Self Hosted Registry') {
            steps {
                script {
                    sh "docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}"
                }
            }
        }

        stage('Verify Image in Registry') {
            steps {
                script {
                    sh "curl http://${REGISTRY}/v2/_catalog"
                }
            }
        }
        stage('Verify The Tags in Repository In Local Registry') {
            steps {
                script {
                    sh "curl http://${REGISTRY}/v2/${REPO_NAME}/tags/list"
                }
            }
        }
        

        stage('Deploy the App') {
            steps {
                script {
                    // Stop and remove if container already running
                    sh """
                        docker rm -f ${CONT_NAME} || true
                        docker run -d -p ${HOST_PORT}:${CONT_PORT} --name ${CONT_NAME} ${REGISTRY}/${IMAGE_NAME}:${TAG}
                    """
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sh "sleep 5" // give app time to start
                    sh "curl -f http://localhost:${HOST_PORT} || echo 'Root endpoint failed'"
                    sh "curl -f http://localhost:${HOST_PORT}/health || echo 'Health endpoint failed'"
                }
            }
        }

    }
}
