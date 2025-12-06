# Object Detection Microservice

A microservice for real-time object detection using YOLOv3.

---

## Quick Start

```bash
# 1. Clone and navigate to project
cd ai-monk-technical-test

# 2. Stop any existing containers and free up ports
docker compose down 2>/dev/null; docker rm -f frontend ui-backend ai-backend 2>/dev/null

# 3. Build and run
docker compose up --build -d

# 4. Wait for services to be ready (about 30 seconds)
echo "Waiting for services..." && sleep 10

# 5. Open in browser
echo "Open http://localhost:3000"
```

---

## Prerequisites

- Docker Engine 20.10+
- Docker Compose V2

### Install Docker

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl start docker && sudo systemctl enable docker
sudo usermod -aG docker $USER
# Log out and log back in after this
```

**Mac/Windows:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

## Deployment

### Start Application
```bash
docker compose up --build -d
```
First build takes a few minutes to download the YOLOv3 model.

### Verify Services are Running
```bash
docker compose ps
```
All 3 services should show "Up" status.

### Access Application
Open **http://localhost:3000** in your browser.

### Stop Application
```bash
docker compose down
```

---

## Troubleshooting

### Port Already in Use
If you get "port already in use" error:
```bash
# Find and kill process on port 3000
sudo lsof -ti:3000 | xargs -r kill -9

# Or stop all containers and retry
docker compose down
docker rm -f $(docker ps -aq) 2>/dev/null
docker compose up --build -d
```

### Clean Restart
For a completely fresh start:
```bash
docker compose down --rmi all --volumes
docker compose up --build -d
```

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f ai-backend
```

---

## Service URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | Web UI |
| UI Backend | http://localhost:5000 | API Gateway |
| AI Backend | http://localhost:5001 | YOLO Detection |
