# 🚀 Quick Start Guide

## Choose Your Deployment Method

### Option 1: Docker (Recommended for Production) 🐳

**Prerequisites:**
- Docker Desktop installed and running

**Steps:**

1. **Start Docker Desktop**
   - Windows: Open Docker Desktop from Start Menu
   - Mac: Open Docker Desktop from Applications
   - Linux: `sudo systemctl start docker`

2. **Navigate to project directory:**
   ```bash
   cd SmartParkingSystem-master/SmartParkingSystem-master
   ```

3. **Run deployment script:**
   
   **Windows:**
   ```bash
   deploy.bat
   ```
   
   **Linux/Mac:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```
   
   **Or manually:**
   ```bash
   docker-compose up -d
   ```

4. **Access the application:**
   - Home: http://localhost:5000
   - Admin: http://localhost:5000/admin/login

5. **Stop the application:**
   ```bash
   docker-compose down
   ```

---

### Option 2: Direct Python (Development) 🐍

**Prerequisites:**
- Python 3.11+ installed

**Steps:**

1. **Navigate to project directory:**
   ```bash
   cd SmartParkingSystem-master/SmartParkingSystem-master
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main_sqlite.py
   ```

4. **Access the application:**
   - Home: http://127.0.0.1:5000
   - Admin: http://127.0.0.1:5000/admin/login

5. **Stop the application:**
   - Press `Ctrl+C` in terminal

---

## 🔐 Default Credentials

### Admin Login
- **URL:** http://localhost:5000/admin/login
- **Username:** `admin`
- **Password:** `admin123`

### User Registration
- Users can register at: http://localhost:5000/login
- Click "Sign Up" tab

---

## 📱 Features Overview

### For Users:
1. Register/Login
2. View available parking slots
3. Make reservations
4. Process payments
5. View reservation history

### For Admins:
1. View all active reservations
2. Use live camera for plate recognition
3. Verify vehicle authorization
4. Monitor parking occupancy

---

## 🎥 Using Camera Feature

1. Login as admin
2. Click "Start Camera" button
3. Allow camera permissions in browser
4. Point camera at license plate
5. Click "Capture & Scan"
6. System will detect and verify plate

**Note:** Camera requires HTTPS in production or localhost for testing.

---

## 🐛 Troubleshooting

### Docker Issues

**Problem:** "Docker is not running"
- **Solution:** Start Docker Desktop

**Problem:** "Port 5000 already in use"
- **Solution:** Stop other services on port 5000 or change port in docker-compose.yml

**Problem:** "Build failed"
- **Solution:** Check Docker Desktop has enough resources (Settings → Resources)

### Python Issues

**Problem:** "Module not found"
- **Solution:** Run `pip install -r requirements.txt`

**Problem:** "Port already in use"
- **Solution:** Stop other Flask apps or change port in main_sqlite.py

### Camera Issues

**Problem:** "Camera not working"
- **Solution:** 
  - Use HTTPS or localhost
  - Grant camera permissions in browser
  - Check if another app is using camera

---

## 📚 Documentation

- **DOCKER_DEPLOYMENT.md** - Complete Docker guide
- **CAMERA_GUIDE.md** - Camera feature guide
- **ADMIN_GUIDE.md** - Admin dashboard guide
- **FEATURES_SUMMARY.md** - All features overview

---

## ✅ Quick Commands

### Docker
```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f

# Restart
docker-compose restart

# Rebuild
docker-compose up -d --build
```

### Python
```bash
# Run
python main_sqlite.py

# Stop
Ctrl+C

# Add test data
python add_test_reservation.py
```

---

## 🎯 Next Steps

1. ✅ Deploy the application
2. ✅ Login as admin
3. ✅ Test camera feature
4. ✅ Create user account
5. ✅ Make a test reservation
6. ✅ Verify with admin dashboard

---

## 📞 Need Help?

Check the documentation files:
- DOCKER_DEPLOYMENT.md for Docker issues
- CAMERA_GUIDE.md for camera problems
- ADMIN_GUIDE.md for admin features

---

**Ready to start? Run the deployment script!**

Windows: `deploy.bat`
Linux/Mac: `./deploy.sh`

🚗✨ Happy Parking!
