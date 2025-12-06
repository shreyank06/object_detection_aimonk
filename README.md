# Object Detection Microservice

A microservice architecture with a UI backend and AI backend. The UI backend accepts image uploads from users, forwards them to the AI backend which uses YOLOv3 for object detection, and returns results in structured JSON format with bounding boxes.

## Install Docker

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl start docker && sudo systemctl enable docker
sudo usermod -aG docker $USER  # Log out and back in after this
```

**macOS/Windows:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quick Start

```bash
docker-compose up --build -d
```
Open
```
http://localhost:3000
```
```
## Services

| Service | Port | Purpose |
|---------|------|---------|
| Frontend | 3000 | Web UI |
| UI Backend | 5000 | REST API |
| AI Backend | 5001 | YOLOv3 inference |

## Usage

1. Open http://localhost:3000
2. Upload an image (drag & drop or click)
3. Click "Detect Objects"
4. View results with bounding boxes

## Commands

```bash
docker-compose logs -f          # View logs
docker-compose down             # Stop
docker-compose down --rmi all --volumes && docker-compose up --build -d  # Clean restart
```

## Troubleshooting

**Port in use:**
```bash
for port in 3000 5000 5001; do sudo lsof -ti:$port | xargs -r kill -9; done
```
