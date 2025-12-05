# Complete Deployment Guide

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│              User's Web Browser                     │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓ HTTP (Port 3000)
┌─────────────────────────────────────────────────────┐
│         Frontend (HTML5/CSS3/JavaScript)            │
│         - Image upload form                         │
│         - Drag & drop support                       │
│         - Results display                           │
│         - Bounding box visualization                │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓ REST API (Port 5000)
┌─────────────────────────────────────────────────────┐
│    UI Backend (Flask + CORS)                        │
│    - Image upload handling                          │
│    - Request routing                                │
│    - Result persistence                             │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓ Internal Network
┌─────────────────────────────────────────────────────┐
│    AI Backend (Flask + OpenCV)                      │
│    - YOLOv3 inference                               │
│    - Bounding box drawing                           │
│    - JSON generation                                │
└─────────────────────────────────────────────────────┘
```

---

## Quick Deployment (3 Commands)

### Step 1: Make script executable
```bash
chmod +x start.sh
```

### Step 2: Start all services
```bash
./start.sh
```

### Step 3: Open in browser
```
http://localhost:3000
```

---

## What Gets Deployed

### Three Docker Containers

| Container | Port | Purpose |
|-----------|------|---------|
| **frontend** | 3000 | Web UI interface |
| **ui-backend** | 5000 | REST API server |
| **ai-backend** | 5001 | YOLOv3 inference |

### Total Resources
- **Estimated Disk**: 2.5 GB (includes model)
- **Memory**: ~1.2 GB (all containers)
- **Startup Time**: 15-30 seconds

---

## Complete Deployment URLs

Once running, access:

```
🌐 FRONTEND:     http://localhost:3000
   ├─ Upload images
   ├─ View detection results
   └─ See confidence scores

🔌 UI BACKEND:   http://localhost:5000
   ├─ /api/detect (POST - submit image)
   ├─ /api/status/<id> (GET - get results)
   └─ /health (GET - health check)

🤖 AI BACKEND:   http://localhost:5001
   ├─ /api/detect (POST - run detection)
   └─ /health (GET - health check)
```

---

## How to Use the Frontend

### Upload Image
1. Open http://localhost:3000 in browser
2. **Option A**: Drag & drop image into the upload area
3. **Option B**: Click the upload area to select file

### Run Detection
1. Click **"🔍 Detect Objects"** button
2. Wait for analysis (5-10 seconds for first image)
3. View results with bounding boxes

### View Results
- **Detection Image**: Shows objects with green bounding boxes
- **Object Count**: Total objects detected
- **Confidence Scores**: Color-coded by confidence level
- **Bounding Box Details**: Exact pixel coordinates

### Reset & Try Again
- Click **"↻ Reset"** to clear and upload new image

---

## Frontend Features

✅ **Drag & Drop**: Drag images directly onto the upload area
✅ **Image Preview**: See image before detection
✅ **Real-time Display**: Results show immediately after detection
✅ **Bounding Boxes**: Visual representation of detected objects
✅ **Confidence Indicators**: Color-coded confidence badges
   - Green: High confidence (80%+)
   - Yellow: Medium confidence (60-79%)
   - Red: Low confidence (<60%)
✅ **Responsive Design**: Works on mobile, tablet, desktop
✅ **Status Messages**: Real-time feedback on operations
✅ **API Status**: Shows backend connectivity status

---

## Step-by-Step Deployment

### Prerequisites
- Docker installed
- Docker Compose installed
- 4GB RAM available
- 500MB free disk space

### Deployment Steps

```bash
# 1. Navigate to project
cd ai-monk-technical-test

# 2. Make startup script executable
chmod +x start.sh

# 3. Run the startup script
./start.sh

# Wait for services to be ready (15-30 seconds)

# 4. Open browser
# Navigate to: http://localhost:3000
```

### What Happens During Startup

```
[1/5] Building Docker images...
      - Builds frontend container
      - Builds UI backend container
      - Builds AI backend container

[2/5] Starting services...
      - Starts all three containers
      - Creates network bridge

[3/5] Waiting for services to be ready...
      - Waits 15 seconds for services to initialize

[4/5] Checking service health...
      - Verifies frontend is responsive
      - Verifies UI backend is responsive
      - Verifies AI backend is responsive

[5/5] Services summary...
      - Shows all service URLs
      - Displays usage instructions
```

---

## Testing the Deployment

### Test Frontend
```bash
# Open in browser
http://localhost:3000
```

### Test UI Backend
```bash
# Health check
curl http://localhost:5000/health

# Expected response
{"status": "healthy", "service": "ui-backend"}
```

### Test AI Backend
```bash
# Health check
curl http://localhost:5001/health

# Expected response
{"status": "healthy", "service": "ai-backend"}
```

### Test Detection API
```bash
# Submit image for detection
curl -X POST -F "image=@sample.jpg" http://localhost:5000/api/detect

# Returns JSON with detection results
```

---

## Useful Commands

### View Running Containers
```bash
docker-compose ps
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f frontend
docker-compose logs -f ui-backend
docker-compose logs -f ai-backend
```

### Stop Services
```bash
docker-compose down
```

### Stop and Remove Everything
```bash
docker-compose down --rmi all
```

### Restart Services
```bash
docker-compose restart
```

### View Resource Usage
```bash
docker stats
```

---

## Troubleshooting

### Frontend Not Loading (http://localhost:3000)

**Issue**: Connection refused on port 3000

**Solutions**:
1. Check if frontend container is running:
   ```bash
   docker-compose ps | grep frontend
   ```

2. View frontend logs:
   ```bash
   docker-compose logs frontend
   ```

3. Verify port is not in use:
   ```bash
   netstat -an | grep 3000
   ```

4. Restart frontend:
   ```bash
   docker-compose restart frontend
   ```

### Backend Not Responding

**Issue**: Cannot connect to backend API

**Solutions**:
1. Check backend health:
   ```bash
   curl http://localhost:5000/health
   ```

2. View backend logs:
   ```bash
   docker-compose logs ui-backend
   docker-compose logs ai-backend
   ```

3. Restart backends:
   ```bash
   docker-compose restart ui-backend ai-backend
   ```

### Model Loading Takes Too Long

**Expected Behavior**: First detection request takes 10-20 seconds as YOLOv3 model loads

**Troubleshooting**:
1. Check logs for progress:
   ```bash
   docker-compose logs -f ai-backend
   ```

2. Be patient - model is downloading/loading (236MB)

3. Subsequent requests will be faster (50-100ms)

### Port Already in Use

**Issue**: Error about port 3000, 5000, or 5001 already in use

**Solution**: Change ports in `docker-compose.yml`:
```yaml
frontend:
  ports:
    - "3001:3000"  # Changed from 3000

ui-backend:
  ports:
    - "5001:5000"  # Changed from 5000

ai-backend:
  ports:
    - "5002:5001"  # Changed from 5001
```

Then access at the new ports (e.g., http://localhost:3001)

### High Memory Usage

**Issue**: Containers using too much memory

**Solutions**:
1. Close other applications
2. Limit Docker resources in Docker Desktop settings
3. Use lighter model (YOLOv3-Tiny)

### Network/Connectivity Issues

**Issue**: Frontend cannot reach backend

**Solutions**:
1. Ensure all containers are running:
   ```bash
   docker-compose ps
   ```

2. Check network:
   ```bash
   docker network ls
   docker network inspect detection-network
   ```

3. Rebuild and restart:
   ```bash
   docker-compose build --no-cache
   docker-compose up -d
   ```

---

## Production Deployment

For production environments, consider:

1. **HTTPS/SSL**: Add nginx reverse proxy with SSL
2. **Authentication**: Add API key/token authentication
3. **Rate Limiting**: Implement request rate limiting
4. **Database**: Persist results in database
5. **Monitoring**: Add Prometheus metrics
6. **Logging**: Centralize logs (ELK stack)
7. **Load Balancing**: Scale with load balancer
8. **Health Checks**: Add comprehensive health monitoring

---

## Performance Tuning

### Optimize Image Upload
- Compress images before uploading
- Recommended max size: 2MB
- Supported formats: JPG, PNG, GIF, BMP

### Optimize Detection
- Model confidence threshold: 0.5 (adjustable)
- NMS threshold: 0.4 (adjustable)
- Inference time: 50-100ms per image

### Optimize Server
- Allocate more CPU cores to containers
- Use SSD for faster I/O
- Increase available RAM

---

## Scaling the Deployment

### Horizontal Scaling
```yaml
# Deploy multiple UI backends with load balancer
ui-backend-1:
  ports:
    - "5000:5000"

ui-backend-2:
  ports:
    - "5001:5000"

ui-backend-3:
  ports:
    - "5002:5000"
```

### Vertical Scaling
Increase Docker resource limits in docker-compose.yml:
```yaml
services:
  ui-backend:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

---

## Support & Documentation

- See **README.md** for complete documentation
- See **API responses** in frontend for detailed detection data
- Check logs for debugging: `docker-compose logs -f`

---

## Success Indicators

When deployment is complete, you should see:

✅ Frontend loads at http://localhost:3000
✅ Upload form is visible and functional
✅ Can drag & drop or select images
✅ Detect Objects button works
✅ Results display with bounding boxes
✅ Confidence scores are shown
✅ All services show as "✓ Running"

---

**Congratulations! Your object detection system is deployed and ready to use!**

