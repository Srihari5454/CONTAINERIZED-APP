🚀 Containerized Flask Application with CI/CD
📌 Project Overview

This project demonstrates how to design, containerize, and automate a simple web application using modern DevOps practices. The application is built with Flask, packaged into a Docker container, orchestrated locally using Docker Compose, and automatically built and pushed to Docker Hub using GitHub Actions.

The focus of this project is on containerization, port management, environment-based configuration, and CI/CD automation.

🛠 Technology Stack

Programming Language: Python

Web Framework: Flask

Containerization: Docker

Local Orchestration: Docker Compose

CI/CD: GitHub Actions

Container Registry: Docker Hub

📂 Project Structure
containerized-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md

⚙️ Application Details
Endpoints
Endpoint	Purpose
/	Displays the application name and the port it is running on
/health	Confirms the application is healthy

The application reads the listening port from an environment variable and exits clearly if the variable is not set.

🌍 Port Configuration and Networking
Ports Used
Layer	Port
Application inside container	8081
Docker container	8081
Host machine	5001
Why Host and Container Ports Are Different

The application always listens on a fixed internal port (8081). Docker maps this port to a host port (5001), allowing flexibility and preventing conflicts with other services.

Traffic Flow
User Browser
   ↓
Host Machine (Port 5001)
   ↓
Docker Port Mapping
   ↓
Container (Port 8081)
   ↓
Flask Application

🐳 Docker Design
Dockerfile Overview

Uses a lightweight Python base image

Runs the application as a non-root user

Accepts the application port through an environment variable

Writes logs to standard output and error streams

Exposes the application port for container networking

Docker Compose Overview

Docker Compose is used to:

Build and run the container locally

Inject environment variables

Map host ports to container ports

Provide a consistent runtime environment

🔄 CI/CD Pipeline Overview

A GitHub Actions pipeline is used to automate:

Source code checkout

Docker image build

Image tagging

Image push to Docker Hub

Container startup and health verification

Docker Hub authentication is handled securely using access tokens.

🔐 Security and Secrets Management

Docker Hub credentials are stored securely as GitHub Actions secrets.
Access tokens are used instead of passwords to follow security best practices.

🧠 Design Decisions
1️⃣ Fixed Internal Application Port

Using a fixed internal port (8081) ensures the container behaves consistently across all environments.

2️⃣ Environment Variable Configuration

Configuration via environment variables keeps the application flexible and avoids hard-coded values.

3️⃣ Docker Compose for Local Orchestration

Docker Compose provides a simple and declarative way to manage container configuration and networking.

🔮 Future Improvements

With more time, the project could be enhanced by:

Replacing the Flask development server with Gunicorn

Adding a Docker HEALTHCHECK

Implementing versioned image tags

Adding automated tests to the CI pipeline

Deploying the application to a Kubernetes cluster

📐 Architecture Diagram
User
 ↓
Browser (localhost:5001)
 ↓
Docker Engine
 ↓
Container (Port 8081)
 ↓
Flask Application

✅ Key Takeaways

Clear understanding of host vs container ports

Proper use of environment variables

Secure Docker Hub authentication

End-to-end container lifecycle automation

🏁 Conclusion

This project showcases a complete and practical example of containerizing an application and integrating CI/CD automation, with a strong emphasis on clarity, security, and best practices.
