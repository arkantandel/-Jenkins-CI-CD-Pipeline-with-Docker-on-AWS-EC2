<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,50:243B55,100:00c6ff&height=220&section=header&text=Jenkins%20CI%2FCD%20Pipeline%20With%20Docker&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Production%20Style%20DevOps%20Implementation&descAlignY=58&descSize=18"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white"/>
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cloud-AWS%20EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
  <img src="https://img.shields.io/badge/OS-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"/>
  <img src="https://img.shields.io/badge/Source-GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

<br/>

---

## 👨‍💻 About The Author

**Arkan Tandel** — DevOps Engineer & Cloud Automation Enthusiast

> Building real pipelines. Solving real problems. Shipping with confidence.

[![GitHub](https://img.shields.io/badge/GitHub-arkantandel-181717?style=flat-square&logo=github)](https://github.com/arkantandel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arkan--tandel-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/arkan-tandel)

---

## 🌟 What Is This Project?

This is a **real-world CI/CD pipeline** built from scratch using **Jenkins + Docker** on an **AWS EC2 Ubuntu** instance. This isn't a tutorial clone — it includes actual errors I hit, how I debugged them, and the production mindset behind every decision.

---

## 🎯 Project Goals

| Goal | Status |
|------|--------|
| Automate the build process | ✅ Done |
| Containerize the application | ✅ Done |
| Connect GitHub → Jenkins → Docker | ✅ Done |
| Solve real production errors | ✅ Done |
| Prepare for cloud deployment | 🔄 In Progress |

---

## 🧩 Technology Stack

| Tool | Role |
|------|------|
| **Jenkins** | CI/CD orchestration engine |
| **Docker + Buildx** | Container build and image management |
| **AWS EC2** | Cloud server hosting the pipeline |
| **Ubuntu** | Host operating system |
| **GitHub** | Source code and trigger for builds |

---

## ⚙️ Pipeline Flow

```
Git Push → Jenkins Trigger → Code Checkout → Docker Build → Test → Deploy
```

Every code push to GitHub automatically kicks off the full pipeline — no manual steps required.

---

## 🛠️ Setup & Installation

### 1. System Prep
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Java + Jenkins
```bash
sudo apt install openjdk-17-jdk -y
sudo apt install jenkins -y
sudo systemctl enable jenkins && sudo systemctl start jenkins
```

### 3. Install Docker
```bash
sudo apt install docker-ce docker-ce-cli containerd.io -y
sudo systemctl enable docker && sudo systemctl start docker
```

### 4. Fix Docker Permissions for Jenkins ⚠️
```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

> **Why this matters:** Jenkins runs as its own user. Without adding it to the `docker` group, it can't communicate with the Docker daemon — your builds will fail silently with a permission error.

---

## 📜 Jenkinsfile (Declarative Pipeline)

```groovy
pipeline {
  agent any

  stages {

    stage('Checkout') {
      steps {
        git url: 'https://github.com/arkantandel/notes-app.git'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t notes-app:latest .'
      }
    }

    stage('Test') {
      steps {
        echo 'Running test suite...'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deployment stage — coming soon'
      }
    }

  }
}
```

---

## 🔥 Real Errors I Hit & Fixed

### ❌ Docker Permission Denied
**Error:** `permission denied while connecting to the Docker daemon socket`  
**Fix:** Added Jenkins to the Docker group — `sudo usermod -aG docker jenkins`

### ❌ Build Context Error
**Error:** Docker couldn't locate the build path  
**Fix:** Corrected the working directory reference in the pipeline

### ❌ Buildx Plugin Crash
**Error:** Docker Buildx plugin failed to initialize  
**Fix:** Removed and reinstalled the Buildx plugin cleanly

---

## 🚀 What's Coming Next

- [ ] Push built image → **AWS ECR**
- [ ] Deploy to **ECS / Kubernetes**
- [ ] Add **automated test coverage**
- [ ] Integrate **security scanning** (Trivy / Snyk)
- [ ] Set up **Slack / email notifications** on build status

---

## 💡 DevOps Philosophy

> *"CI/CD isn't just about automation. It's about building the confidence to ship fast, fix fast, and sleep well."*

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,50:243B55,100:141E30&height=120&section=footer"/>
</p>
