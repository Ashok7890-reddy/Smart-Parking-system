#!/bin/bash

echo "============================================================"
echo "  ParkFind Smart Parking System - Docker Deployment"
echo "============================================================"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "[ERROR] Docker is not running!"
    echo ""
    echo "Please start Docker and try again."
    echo ""
    exit 1
fi

echo "[1/5] Docker is running..."
echo ""

echo "[2/5] Building Docker image..."
docker-compose build
if [ $? -ne 0 ]; then
    echo "[ERROR] Build failed!"
    exit 1
fi
echo ""

echo "[3/5] Starting containers..."
docker-compose up -d
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to start containers!"
    exit 1
fi
echo ""

echo "[4/5] Waiting for application to start..."
sleep 5
echo ""

echo "[5/5] Checking container status..."
docker-compose ps
echo ""

echo "============================================================"
echo "  Deployment Successful!"
echo "============================================================"
echo ""
echo "Application is running at:"
echo "  - Home: http://localhost:5000"
echo "  - User Login: http://localhost:5000/login"
echo "  - Admin Login: http://localhost:5000/admin/login"
echo ""
echo "Admin Credentials:"
echo "  - Username: admin"
echo "  - Password: admin123"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"
echo ""
