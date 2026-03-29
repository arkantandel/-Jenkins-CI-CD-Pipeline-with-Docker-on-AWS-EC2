<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,50:243B55,100:00c6ff&height=220&section=header&text=Jenkins%20CI%2FCD%20Pipeline%20With%20Docker&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Production%20Style%20DevOps%20Implementation%20on%20AWS%20EC2&descAlignY=58&descSize=18"/>
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

**Arkan Tandel** — Cloud & DevOps Engineer

> Building real pipelines. Solving real problems. Shipping with confidence.

[![GitHub](https://img.shields.io/badge/GitHub-arkantandel-181717?style=flat-square&logo=github)](https://github.com/arkantandel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arkan--tandel-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/arkan-tandel)

---

## 🌟 What Is This Project?

This is a **real-world CI/CD pipeline** built from scratch using **Jenkins + Docker** on an **AWS EC2 Ubuntu** instance.

This is **not a tutorial clone** — it includes:
- ✅ Actual errors I encountered and debugged
- ✅ Production mindset behind every decision
- ✅ Step-by-step setup from zero to working pipeline

---

## 🎯 Project Goals

| Goal | Status |
|------|--------|
| Automate the build process | ✅ Done |
| Containerize the application | ✅ Done |
| Connect GitHub → Jenkins → Docker | ✅ Done |
| Solve real production errors | ✅ Done |
| Push image to AWS ECR | 🔄 In Progress |
| Deploy to ECS / Kubernetes | 🔄 In Progress |

---

## 🧩 Technology Stack

| Tool | Role |
|------|------|
| **Jenkins** | CI/CD orchestration engine |
| **Docker + Buildx** | Container build and image management |
| **AWS EC2** | Cloud server hosting the pipeline |
| **Ubuntu 22.04** | Host operating system |
| **GitHub** | Source code and webhook trigger |

---

## 🏗️ System Architecture

```
Developer
    │
    │  git push (main branch)
    ▼
 GitHub
    │
    │  webhook trigger
    ▼
 Jenkins (AWS EC2 Ubuntu)
    │
    ├── Stage 1: Checkout Code
    ├── Stage 2: Docker Build
    ├── Stage 3: Test
    └── Stage 4: Deploy
         │
         ▼
      Docker Container (Running App)
         │
         ▼
      AWS ECR → ECS / Kubernetes  (coming soon)
```

---

## ⚙️ Pipeline Flow

```
Git Push → Jenkins Trigger → Code Checkout → Docker Build → Test → Deploy
```

Every code push to GitHub **automatically kicks off the full pipeline** — no manual steps required.

---

## 🛠️ Setup & Installation

### Step 1 — Launch AWS EC2 Instance

- AMI: **Ubuntu 22.04 LTS**
- Instance Type: **t2.medium** (minimum 2GB RAM for Jenkins)
- Security Group: Open ports **22** (SSH), **8080** (Jenkins), **80** (HTTP)

```bash
# Connect to your EC2 instance
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<your-ec2-public-ip>

# Update system packages
sudo apt update && sudo apt upgrade -y
```

---

### Step 2 — Install Java (Jenkins Dependency)

```bash
sudo apt install openjdk-17-jdk -y

# Verify installation
java -version
# Expected: openjdk version "17.x.x"
```

---

### Step 3 — Install Jenkins

```bash
# Add official Jenkins GPG key
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key \
  | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

# Add Jenkins repository
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ \
  | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Install Jenkins
sudo apt update
sudo apt install jenkins -y

# Enable and start Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins

# Check status
sudo systemctl status jenkins
```

> **Access Jenkins UI:** Open `http://<your-ec2-ip>:8080` in browser
>
> **Get initial admin password:**
> ```bash
> sudo cat /var/lib/jenkins/secrets/initialAdminPassword
> ```

---

### Step 4 — Install Docker

```bash
# Install dependencies
sudo apt install ca-certificates curl gnupg lsb-release -y

# Add Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y

# Start Docker
sudo systemctl enable docker
sudo systemctl start docker

# Verify
docker --version
```

---

### Step 5 — ⚠️ Fix Docker Permissions for Jenkins (CRITICAL)

> This is the **#1 error** DevOps beginners hit. Do NOT skip this step.

```bash
# Add jenkins user to docker group
sudo usermod -aG docker jenkins

# Restart Jenkins to apply changes
sudo systemctl restart jenkins

# Verify
grep docker /etc/group
# Expected output: docker:x:999:jenkins
```

**Why this is needed:** Jenkins runs as its own system user (`jenkins`). The Docker daemon socket at `/var/run/docker.sock` only accepts connections from the `docker` group. Without this, every build fails with a permission error.

---

## 📜 Jenkinsfile (Declarative Pipeline)

```groovy
pipeline {
  agent any

  environment {
    IMAGE_NAME = 'notes-app'
    IMAGE_TAG  = 'latest'
  }

  stages {

    stage('Checkout') {
      steps {
        git url: 'https://github.com/arkantandel/notes-app.git',
            branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
      }
    }

    stage('Test') {
      steps {
        echo 'Running test suite...'
        sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} npm test'
      }
    }

    stage('Deploy') {
      steps {
        sh '''
          docker stop notes-app-container || true
          docker rm   notes-app-container || true
          docker run -d -p 80:3000 --name notes-app-container \
            ${IMAGE_NAME}:${IMAGE_TAG}
        '''
      }
    }

  }

  post {
    success { echo 'Pipeline succeeded — app is live!' }
    failure { echo 'Pipeline failed — check the logs above' }
  }
}
```

---

## 🔥 Real Errors I Hit & Fixed

### ❌ Error 1 — Docker Permission Denied

```
Got permission denied while trying to connect to the Docker daemon socket
at unix:///var/run/docker.sock
```

**Root Cause:** Jenkins user not in docker group

**Fix:**
```bash
sudo usermod -aG docker jenkins && sudo systemctl restart jenkins
```

---

### ❌ Error 2 — Build Context Error

```
unable to evaluate symlinks in Dockerfile path: no such file or directory
```

**Root Cause:** Docker build running from wrong working directory

**Fix:** Add `dir()` block in Jenkinsfile
```groovy
dir('notes-app') {
  sh 'docker build -t notes-app:latest .'
}
```

---

### ❌ Error 3 — Docker Buildx Plugin Crash

```
ERROR: failed to solve: failed to read dockerfile — buildx plugin failed
```

**Root Cause:** Buildx plugin corrupted after system update

**Fix:**
```bash
# Remove corrupted plugin
rm -rf ~/.docker/cli-plugins/docker-buildx

# Reinstall
sudo apt install --reinstall docker-buildx-plugin -y

# Verify
docker buildx version
```

---

## 🚀 What's Coming Next

- [ ] Push built image → **AWS ECR**
- [ ] Deploy to **ECS / Kubernetes**
- [ ] Add **automated test coverage**
- [ ] Integrate **Trivy security scanning**
- [ ] Set up **Slack / email notifications** on build status
- [ ] **Prometheus + Grafana** pipeline monitoring

---

## 💡 DevOps Philosophy

> *"CI/CD isn't just about automation. It's about building the confidence to ship fast, fix fast, and sleep well."*

---

## 📁 Repository Structure

```
.
├── Code-Files/
│   └── Jenkins.file        # Declarative pipeline definition
├── LICENSE
└── README.md               # This file
```

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,50:243B55,100:141E30&height=120&section=footer"/>
</p>

