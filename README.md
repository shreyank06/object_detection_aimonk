# Object Detection Microservice

A microservice for real-time object detection using YOLOv3.

---

## Prerequisites

- Docker Engine 20.10+
- Docker Compose V2

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

```bash
# Navigate to project
cd ai-monk-technical-test

# Build and run
docker compose up --build -d

# Verify all services are running
docker compose ps
```

First build takes a few minutes to download the YOLOv3 model.

**Access Application:** http://localhost:3000

**Stop Application:**
```bash
docker compose down
```

---

## Troubleshooting

**Port already in use:**
```bash
sudo lsof -ti:3000 | xargs -r kill -9
docker compose up --build -d
```

**Clean restart:**
```bash
docker compose down --rmi all --volumes
docker compose up --build -d
```

**View logs:**
```bash
docker compose logs -f
```

---

## Service URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| UI Backend | http://localhost:5000 |
| AI Backend | http://localhost:5001 |
