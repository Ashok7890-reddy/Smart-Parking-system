# 🐳 Docker Deployment Guide

## 📋 Prerequisites

Before deploying with Docker, ensure you have:

- **Docker Desktop** installed (Windows/Mac) or **Docker Engine** (Linux)
- **Docker Compose** installed (usually comes with Docker Desktop)
- At least **500MB** free disk space
- **Port 5000** available on your system

### Check Docker Installation

```bash
docker --version
docker-compose --version
```

Expected output:
```
Docker version 24.x.x
Docker Compose version v2.x.x
```

## 🚀 Quick Start (Easiest Method)

### Option 1: Using Docker Compose (Recommended)

1. **Navigate to project directory:**
```bash
cd SmartParkingSystem-master/SmartParkingSystem-master
```

2. **Build and start the container:**
```bash
docker-compose up -d
```

3. **Access the application:**
- Home: http://localhost:5000
- User Login: http://localhost:5000/login
- Admin Login: http://localhost:5000/admin/login

4. **View logs:**
```bash
docker-compose logs -f
```

5. **Stop the application:**
```bash
docker-compose down
```

### Option 2: Using Docker Commands

1. **Build the Docker image:**
```bash
docker build -t parkfind-app .
```

2. **Run the container:**
```bash
docker run -d -p 5000:5000 --name parkfind parkfind-app
```

3. **Access the application:**
- http://localhost:5000

4. **Stop the container:**
```bash
docker stop parkfind
docker rm parkfind
```

## 📦 What's Included

### Docker Files

1. **Dockerfile**
   - Base image: Python 3.11 slim
   - Installs all dependencies
   - Sets up the application
   - Exposes port 5000
   - Includes health check

2. **docker-compose.yml**
   - Service configuration
   - Port mapping
   - Volume mounting
   - Network setup
   - Auto-restart policy

3. **.dockerignore**
   - Excludes unnecessary files
   - Reduces image size
   - Improves build speed

4. **requirements.txt**
   - Flask 3.0.2
   - Werkzeug 3.0.1
   - Requests 2.31.0

## 🔧 Configuration

### Environment Variables

You can customize the deployment using environment variables:

```yaml
environment:
  - FLASK_APP=main_sqlite.py
  - FLASK_ENV=production  # or 'development' for debug mode
```

### Port Configuration

To use a different port, modify `docker-compose.yml`:

```yaml
ports:
  - "8080:5000"  # Access on port 8080 instead of 5000
```

### Volume Mounting

The database is persisted using volumes:

```yaml
volumes:
  - ./data:/app/data          # Data directory
  - ./parking.db:/app/parking.db  # SQLite database
```

## 📊 Container Management

### View Running Containers
```bash
docker ps
```

### View All Containers
```bash
docker ps -a
```

### View Container Logs
```bash
docker logs parkfind-app
docker logs -f parkfind-app  # Follow logs
```

### Execute Commands in Container
```bash
docker exec -it parkfind-app bash
```

### Restart Container
```bash
docker restart parkfind-app
```

### Stop Container
```bash
docker stop parkfind-app
```

### Remove Container
```bash
docker rm parkfind-app
```

### Remove Image
```bash
docker rmi parkfind-app
```

## 🔄 Updating the Application

### Method 1: Using Docker Compose

```bash
# Stop and remove containers
docker-compose down

# Rebuild with latest changes
docker-compose up -d --build
```

### Method 2: Manual Update

```bash
# Stop container
docker stop parkfind-app
docker rm parkfind-app

# Rebuild image
docker build -t parkfind-app .

# Run new container
docker run -d -p 5000:5000 --name parkfind-app parkfind-app
```

## 🗄️ Database Management

### Backup Database

```bash
# Copy database from container
docker cp parkfind-app:/app/parking.db ./backup_parking.db
```

### Restore Database

```bash
# Copy database to container
docker cp ./backup_parking.db parkfind-app:/app/parking.db

# Restart container
docker restart parkfind-app
```

### Add Test Data

```bash
# Execute Python script in container
docker exec parkfind-app python add_test_reservation.py
```

## 🌐 Production Deployment

### Using Docker Compose (Production)

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  parkfind:
    build: .
    container_name: parkfind-prod
    ports:
      - "80:5000"
    volumes:
      - parkfind-data:/app/data
      - parkfind-db:/app
    environment:
      - FLASK_ENV=production
    restart: always
    networks:
      - parkfind-network

volumes:
  parkfind-data:
  parkfind-db:

networks:
  parkfind-network:
    driver: bridge
```

Deploy:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### With Nginx Reverse Proxy

Create `nginx.conf`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://parkfind:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Update `docker-compose.yml`:

```yaml
services:
  parkfind:
    # ... existing config ...
    expose:
      - "5000"
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - parkfind
    networks:
      - parkfind-network
```

## 🔒 Security Best Practices

### 1. Change Default Credentials

Update admin credentials in `main_sqlite.py`:

```python
# Change from:
if username == 'admin' and password == 'admin123':

# To:
if username == 'admin' and password == 'your-secure-password':
```

### 2. Use Environment Variables

Store sensitive data in `.env` file:

```bash
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure_password_here
SECRET_KEY=your-secret-key-here
```

Update `docker-compose.yml`:

```yaml
services:
  parkfind:
    env_file:
      - .env
```

### 3. Enable HTTPS

Use Let's Encrypt with Nginx for SSL/TLS:

```bash
docker run -d \
  --name certbot \
  -v /etc/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly --standalone -d your-domain.com
```

## 📈 Monitoring & Health Checks

### Health Check Status

```bash
docker inspect --format='{{.State.Health.Status}}' parkfind-app
```

### Container Stats

```bash
docker stats parkfind-app
```

### Resource Usage

```bash
docker system df
```

## 🐛 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs parkfind-app

# Check if port is in use
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # Linux/Mac
```

### Database Issues

```bash
# Reset database
docker exec parkfind-app rm /app/parking.db
docker restart parkfind-app
```

### Permission Issues

```bash
# Fix permissions (Linux/Mac)
sudo chown -R $USER:$USER .
```

### Build Failures

```bash
# Clean build cache
docker builder prune

# Rebuild without cache
docker-compose build --no-cache
```

## 📱 Accessing from Other Devices

### Same Network

1. Find your computer's IP address:
   - Windows: `ipconfig`
   - Linux/Mac: `ifconfig` or `ip addr`

2. Access from other devices:
   - http://YOUR_IP_ADDRESS:5000

### Port Forwarding (Router)

1. Forward port 5000 to your computer's local IP
2. Access using your public IP or domain

## 🔄 CI/CD Integration

### GitHub Actions Example

Create `.github/workflows/docker.yml`:

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build Docker image
        run: docker build -t parkfind-app .
      
      - name: Run tests
        run: docker run parkfind-app python -m pytest
```

## 📊 Performance Optimization

### Reduce Image Size

```dockerfile
# Use multi-stage build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main_sqlite.py"]
```

### Enable Caching

```bash
docker-compose build --parallel
```

## 🎯 Quick Commands Reference

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Restart
docker-compose restart

# View logs
docker-compose logs -f

# Rebuild
docker-compose up -d --build

# Clean up
docker-compose down -v
docker system prune -a
```

## 📞 Support

### Common Issues

1. **Port already in use**: Change port in docker-compose.yml
2. **Permission denied**: Run with sudo (Linux) or check Docker Desktop
3. **Database locked**: Restart container
4. **Camera not working**: Use HTTPS or localhost

### Getting Help

- Check logs: `docker-compose logs`
- Inspect container: `docker inspect parkfind-app`
- Test connectivity: `docker exec parkfind-app curl localhost:5000`

---

## ✅ Deployment Checklist

- [ ] Docker and Docker Compose installed
- [ ] Port 5000 available
- [ ] Project files in correct directory
- [ ] Database backed up (if existing)
- [ ] Admin credentials changed
- [ ] Environment variables configured
- [ ] Build successful
- [ ] Container running
- [ ] Application accessible
- [ ] Camera permissions granted (for admin)
- [ ] Test reservations working
- [ ] Logs monitored

---

**Quick Start Command:**
```bash
docker-compose up -d && docker-compose logs -f
```

**Access Application:**
- http://localhost:5000

**Admin Login:**
- Username: admin
- Password: admin123 (change this!)

Happy Deploying! 🐳🚗✨
