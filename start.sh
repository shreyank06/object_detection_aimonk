#!/bin/bash

# Object Detection Microservice Startup Script

set -e

echo "================================================"
echo "Object Detection Microservice - Startup"
echo "================================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "ERROR: Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "[1/5] Building Docker images..."
docker-compose build

echo ""
echo "[2/5] Starting services..."
docker-compose up -d

echo ""
echo "[3/5] Waiting for services to be ready..."
sleep 15

echo ""
echo "[4/5] Checking service health..."

# Check Frontend
echo -n "Frontend: "
if curl -s http://localhost:3000 > /dev/null 2>&1; then
    echo "✓ Running"
else
    echo "✗ Not responding"
fi

# Check UI Backend
echo -n "UI Backend: "
if curl -s http://localhost:5000/health > /dev/null 2>&1; then
    echo "✓ Running"
else
    echo "✗ Not responding"
fi

# Check AI Backend
echo -n "AI Backend: "
if curl -s http://localhost:5001/health > /dev/null 2>&1; then
    echo "✓ Running"
else
    echo "✗ Not responding (this may take a moment for model loading)"
fi

echo ""
echo "[5/5] Services summary:"
echo "================================================"
echo "✅ All services started successfully!"
echo "================================================"
echo ""
echo "🌐 FRONTEND:     http://localhost:3000"
echo "🔌 UI Backend:   http://localhost:5000"
echo "🤖 AI Backend:   http://localhost:5001"
echo ""
echo "📖 How to use:"
echo "  1. Open http://localhost:3000 in your browser"
echo "  2. Drag and drop an image or click to upload"
echo "  3. Click 'Detect Objects' button"
echo "  4. View results with bounding boxes"
echo ""
echo "🔧 Useful commands:"
echo "  View logs:           docker-compose logs -f"
echo "  Stop services:       docker-compose down"
echo "  Check container IDs: docker-compose ps"
echo ""
