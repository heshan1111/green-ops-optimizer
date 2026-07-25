# 🚀 GreenOps Optimizer

> **AI-Powered Resource Optimization Platform**

GreenOps Optimizer is a Python-based DevOps project that automatically monitors system resource usage and makes optimization decisions to improve infrastructure efficiency.

This project combines **FastAPI**, **Prometheus**, **Grafana**, **Docker**, and **Python** to demonstrate GreenOps principles and cloud-native monitoring.

---

# 📖 Project Overview

GreenOps Optimizer continuously collects system metrics from Prometheus and evaluates CPU usage using a simple decision engine.

Depending on CPU utilization, the optimizer selects one of three operating modes:

- 🌿 ECO Mode
- ⚖️ BALANCED Mode
- ⚡ PERFORMANCE Mode

The project is designed as a learning project for DevOps, Cloud Computing, and Monitoring technologies.

---

# ✨ Features

- ✅ FastAPI Backend
- ✅ Prometheus Metrics Integration
- ✅ Docker Container Monitoring
- ✅ Grafana Dashboard
- ✅ Automatic CPU Decision Engine
- ✅ Docker-based Deployment
- ✅ Git Version Control

---

# 🏗️ System Architecture

```text
                +------------------+
                |     FastAPI      |
                +---------+--------+
                          |
                          |
                          v
                +------------------+
                |   Prometheus     |
                +---------+--------+
                          |
                          |
                          v
                +------------------+
                | Decision Engine  |
                +---------+--------+
                          |
                          |
                          v
                +------------------+
                | Docker Optimizer |
                +------------------+
```

---

# ⚙️ Decision Rules

| CPU Usage | Mode |
|-----------|------|
| <20% | ECO |
| 20% - 70% | BALANCED |
| >70% | PERFORMANCE |

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Prometheus
- Grafana
- Docker
- Docker Compose
- Git
- GitHub

---

# 📂 Project Structure

```text
green-ops-optimizer/

│
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── optimizer/
│   ├── decision_engine.py
│   ├── docker_service.py
│   ├── prometheus_service.py
│   ├── engine.py
│   └── Dockerfile
│
├── docker-compose.yml
├── prometheus.yml
└── .gitignore
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/heshan1111/green-ops-optimizer.git
```

---

## Start Containers

```bash
docker compose up --build
```

---

## FastAPI

```
http://localhost:8000
```

API Documentation

```
http://localhost:8000/docs
```

---

## Prometheus

```
http://localhost:9090
```

---

## Grafana

```
http://localhost:3000
```

---

# 📊 Monitoring

Current monitoring includes:

- CPU Usage
- Prometheus Metrics
- Docker Monitoring

Future versions will include:

- Memory Monitoring
- Network Monitoring
- Disk Monitoring
- Container Health Monitoring

---

# 🗺️ Roadmap

## ✅ Sprint 1 (Completed)

- FastAPI
- Docker
- Prometheus
- Grafana
- CPU Decision Engine
- GitHub Integration
- Version v1.0.0

---

## 🚧 Sprint 2 (In Progress)

- Logging System
- Environment Variables
- Memory Monitoring
- Health Checks
- Better Dashboard

---

## 📌 Future Goals

- Kubernetes Deployment
- CI/CD Pipeline
- AI-based Prediction
- AWS Deployment
- Slack Notifications
- Auto Scaling

---

# 📄 License

This project is created for educational and portfolio purposes.

---

# 👨‍💻 Author

**Heshan Fernando**

University of Vavuniya

Aspiring DevOps Engineer
