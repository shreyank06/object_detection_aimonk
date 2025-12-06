# Object Detection Microservice

Real-time object detection using YOLOv3.

## Quick Start

```bash
# Build and run
docker-compose up --build -d

# Open in browser
# http://localhost:3000
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
# View logs
docker-compose logs -f

# Stop
docker-compose down

# Clean restart
docker-compose down --rmi all --volumes
docker-compose up --build -d
```

## Troubleshooting

**Port in use:**
```bash
for port in 3000 5000 5001; do
  sudo lsof -ti:$port | xargs -r kill -9
done
```
