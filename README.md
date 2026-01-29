<!-- 🚀 ULTRA CI/CD BANNER -->

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,50:243B55,100:00c6ff&height=250&section=header&text=Jenkins%20CI/CD%20Pipeline%20With%20Docker&fontSize=42&fontColor=ffffff&animation=fadeIn"/>
</p>

---

# 🚀 Jenkins CI/CD Pipeline with Docker on Ubuntu

<h3 align="center">Production Style DevOps CI/CD Implementation</h3>

---

<p align="center">

<img src="https://img.shields.io/badge/CI/CD-Jenkins-red?style=for-the-badge&logo=jenkins"/>
<img src="https://img.shields.io/badge/Container-Docker-blue?style=for-the-badge&logo=docker"/>
<img src="https://img.shields.io/badge/Cloud-AWS-orange?style=for-the-badge&logo=amazonaws"/>
<img src="https://img.shields.io/badge/Source-GitHub-black?style=for-the-badge&logo=github"/>
<img src="https://img.shields.io/badge/Level-Production%20Ready-green?style=for-the-badge"/>

</p>

---

# 👨‍💻 Project Owner

**Arkan Tandel**  
DevOps Engineer | Cloud Automation Enthusiast 🚀  

GitHub → https://github.com/arkantandel  
LinkedIn → https://linkedin.com/in/arkan-tandel  

---

# 🌟 Project Vision

This project demonstrates **real-world CI/CD pipeline implementation** using Jenkins and Docker on Ubuntu running inside AWS EC2.

This is not just setup —  
This represents **real DevOps troubleshooting + pipeline design + production mindset**.

---

# 📌 Project Goal

✔ Automate Build Process  
✔ Containerize Application  
✔ Integrate GitHub → Jenkins → Docker  
✔ Prepare for Cloud Deployment  
✔ Solve Real Production Errors  

---

# 🏗️ High Level CI/CD Architecture

```mermaid
flowchart LR
    Dev[Developer] --> GitHub
    GitHub --> Jenkins
    Jenkins --> DockerBuild
    DockerBuild --> DockerImage
    DockerImage --> Deployment
```

---

# 🔄 Pipeline Execution Flow

```mermaid
flowchart TD
    Push[Git Push] --> Trigger[Jenkins Trigger]
    Trigger --> Checkout[Checkout Code]
    Checkout --> Build[Docker Build]
    Build --> Test[Test Stage]
    Test --> Deploy[Deploy Stage]
```

---

# 🧩 Technology Stack

| Tool | Purpose |
|---|---|
Jenkins | CI/CD Automation |
Docker | Containerization |
Docker Buildx | Advanced Build Engine |
GitHub | Source Code |
Ubuntu | CI/CD Host OS |
AWS EC2 | Cloud Infrastructure |

---

# ⚙ Jenkins Installation (Ubuntu)

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
```

```bash
sudo apt install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

---

# 🐳 Docker Installation

```bash
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

---

# 🔑 Critical Production Fix — Docker Permission

### ❌ Error
permission denied while connecting to Docker daemon

### ✅ Solution

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

# 🧱 Docker Buildx Architecture

```mermaid
flowchart LR
    DockerCLI --> BuildxPlugin
    BuildxPlugin --> BuildKitEngine
    BuildKitEngine --> DockerImage
```

---

# 📂 Jenkins Workspace Structure

```mermaid
flowchart TD
    Workspace --> SourceCode
    SourceCode --> Dockerfile
    SourceCode --> Jenkinsfile
```

---

# 📜 Jenkins Pipeline (Declarative)

```groovy
pipeline {
 agent any

 stages {
  stage('Checkout') {
   steps {
    git url: 'https://github.com/arkantandel/...git'
   }
  }

  stage('Build') {
   steps {
    sh 'docker build -t notes-app:latest .'
   }
  }

  stage('Test') {
   steps {
    echo 'Testing Phase'
   }
  }

  stage('Deploy') {
   steps {
    echo 'Future Deployment Stage'
   }
  }
 }
}
```

---

# ❌ Real Errors I Faced (Production Style)

### Docker Permission Issue  
Solved using Docker group access  

### Build Context Error  
Fixed build path  

### Buildx Plugin Error  
Reinstalled plugin properly  

---

# 🧠 Jenkins Internal Execution

```mermaid
flowchart LR
    JenkinsMaster --> Executor
    Executor --> Workspace
    Workspace --> Shell
    Shell --> DockerEngine
```

---

# 🛠 Real Commands I Executed

### System Prep
```bash
sudo apt update && sudo apt upgrade -y
```

---

### Docker Install
```bash
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

---

### Jenkins Install
```bash
sudo apt install jenkins -y
```

---

### Jenkins Docker Permission
```bash
sudo usermod -aG docker jenkins
```

---

# 🌟 What This Project Proves

✔ Real CI/CD Implementation  
✔ Real Troubleshooting Skills  
✔ Linux Permission Understanding  
✔ Docker Internal Knowledge  
✔ Production Pipeline Thinking  

---

# 🚀 Future Enterprise Improvements

✔ Push Image → AWS ECR  
✔ Deploy → ECS / Kubernetes  
✔ Add Automated Tests  
✔ Add Security Scan  

---

# ❤️ DevOps Philosophy

> CI/CD is not about automation only.  
> It is about reliability, speed, and confidence in deployments.

---

<!-- FOOTER -->

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,50:243B55,100:141E30&height=120&section=footer"/>
</p>

