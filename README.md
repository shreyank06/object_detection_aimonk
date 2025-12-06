# Object Detection Microservice

A microservice for real-time object detection using YOLOv3.

---

## Docker Deployment

### Prerequisites
- Docker and Docker Compose installed on your machine

### Step 1: Install Docker (Skip if already installed)

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```
*Log out and log back in after running the above commands.*

**Mac:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

**Windows:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Step 2: Navigate to Project
```bash
cd ai-monk-technical-test
```

### Step 3: Build and Run
```bash
docker compose up --build
```

Wait for the build to complete (first time takes a few minutes to download YOLOv3 model).

### Step 4: Access the Application

Open your browser and go to: **http://localhost:3000**

### Stop the Application
```bash
docker compose down
```

### Quick Reference Commands
```bash
# Start services (background mode)
docker compose up -d

# View logs
docker compose logs -f

# Check running containers
docker compose ps

# Restart services
docker compose restart

# Full cleanup (removes images too)
docker compose down --rmi all
```

---

## Service URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| UI Backend | http://localhost:5000 |
| AI Backend | http://localhost:5001 |
