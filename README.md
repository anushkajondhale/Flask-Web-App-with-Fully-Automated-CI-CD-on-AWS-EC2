# Flask Web App with Automated CI/CD Pipeline on AWS EC2

This project demonstrates the deployment of a **Flask web application** using **Docker**, with a fully automated **CI/CD pipeline** powered by **Jenkins** and hosted on **AWS EC2**.  

The pipeline automates:
- Building Docker images for the Flask app  
- Running tests (optional)  
- Pushing the image to Docker Hub (or any container registry)  
- Deploying the updated container on AWS EC2  

---

## 🚀 Architecture Overview

1. **Flask Application** – A simple Python web app serving as the base application.  
2. **Docker** – Containerizes the Flask app for consistency across environments.  
3. **Jenkins** – Manages CI/CD pipeline (build → test → push → deploy).  
4. **AWS EC2** – Hosts Jenkins server and runs the Dockerized Flask app.  

**Workflow:**  
Developer pushes code → Jenkins detects changes → Jenkins builds Docker image → Pushes to registry → Deploys on EC2 → Live update!

---

## 🛠️ Tech Stack

- **Flask (Python)** – Backend framework  
- **Docker** – Containerization  
- **Jenkins** – Continuous Integration/Continuous Deployment  
- **AWS EC2** – Hosting infrastructure  
- **GitHub/GitLab** – Source code repository  
- **Docker Hub / ECR** – Container registry  

---

## 📂 Project Structure

flask-cicd-app/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build file
├── Jenkinsfile # Jenkins pipeline definition
├── scripts/
│ └── deploy.sh # Deployment script for EC2
└── README.md # Project documentation
