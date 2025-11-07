# 🚗 ParkFind - Smart Parking System

A modern, feature-rich smart parking management system with live camera-based number plate recognition, built with Flask and deployed with Docker.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎨 Beautiful Modern UI
- Gradient purple theme with smooth animations
- Fully responsive design (mobile, tablet, desktop)
- Professional card-based layouts
- Icon-enhanced interfaces

### 👥 User Features
- **Registration & Login** - Secure authentication system
- **Real-time Dashboard** - Live parking slot availability
- **Smart Reservations** - Easy booking with date/time selection
- **Payment Processing** - Integrated billing system (₹20/hour)
- **Reservation History** - Track all bookings

### 🛡️ Admin Features
- **Separate Admin Portal** - Dedicated management interface
- **Active Reservations Table** - Real-time monitoring of all bookings
- **Live Camera Feed** - Access device camera for plate scanning
- **OCR Technology** - Automatic number plate recognition using Tesseract.js
- **Instant Verification** - Real-time authorization checks
- **Visual & Audio Feedback** - Color-coded results with beep sounds

### 📷 Number Plate Recognition
- Live camera feed from device
- Automatic OCR detection
- Pattern matching and validation
- Auto-fill detected plates
- Manual entry fallback
- Works on all devices with camera

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Start Docker Desktop**

2. **Run deployment script:**
   ```bash
   # Windows
   deploy.bat
   
   # Linux/Mac
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Access application:**
   - Home: http://localhost:5000
   - Admin: http://localhost:5000/admin/login

### Option 2: Python Direct

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run application:**
   ```bash
   python main_sqlite.py
   ```

3. **Access application:**
   - Home: http://127.0.0.1:5000

## 🔐 Default Credentials

**Admin Login:**
- Username: `admin`
- Password: `admin123`

**Users:** Register at /login (Sign Up tab)

## 📁 Project Structure

```
SmartParkingSystem-master/
├── templates/              # HTML templates
│   ├── index.html         # Home page
│   ├── login.html         # User login/register
│   ├── dashboard.html     # User dashboard
│   ├── reservation.html   # Booking page
│   ├── payment.html       # Payment page
│   ├── admin_login.html   # Admin login
│   └── admin_dashboard.html # Admin panel with camera
├── static/                # Static assets (CSS, JS, images)
├── main_sqlite.py         # Main Flask application
├── parking.db             # SQLite database
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose config
├── requirements.txt       # Python dependencies
├── deploy.bat             # Windows deployment script
├── deploy.sh              # Linux/Mac deployment script
└── *.md                   # Documentation files
```

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.2** - Web framework
- **SQLite** - Database
- **Python 3.11+** - Programming language

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling (gradients, flexbox, grid)
- **JavaScript** - Interactivity
- **Tesseract.js** - OCR engine
- **Font Awesome 6.0** - Icons

### Deployment
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- **[DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)** - Complete Docker guide
- **[CAMERA_GUIDE.md](CAMERA_GUIDE.md)** - Camera feature documentation
- **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - Admin dashboard guide
- **[FEATURES_SUMMARY.md](FEATURES_SUMMARY.md)** - All features overview
- **[UI_IMPROVEMENTS.md](UI_IMPROVEMENTS.md)** - UI design details

## 🎯 Use Cases

### For Parking Lot Operators
- Monitor real-time occupancy
- Verify vehicle authorization
- Quick plate scanning at entry
- Track reservations and payments

### For Drivers
- Find available parking spots
- Reserve slots in advance
- View pricing and duration
- Make secure payments

### For Security Guards
- Scan license plates with camera
- Instant authorization checks
- Audio/visual feedback
- Direct vehicles to assigned slots

## 🐳 Docker Commands

```bash
# Start application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop application
docker-compose down

# Rebuild and restart
docker-compose up -d --build

# Check status
docker-compose ps
```

## 🔧 Configuration

### Change Admin Password
Edit `main_sqlite.py`:
```python
if username == 'admin' and password == 'YOUR_NEW_PASSWORD':
```

### Change Port
Edit `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # Use port 8080 instead
```

### Database Location
Database file: `parking.db` (SQLite)
Backup: `docker cp parkfind-app:/app/parking.db ./backup.db`

## 📱 Browser Support

- ✅ Chrome (recommended for camera)
- ✅ Firefox
- ✅ Edge
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Android Chrome)

## 🔒 Security Features

- Session-based authentication
- Admin/User role separation
- SQL injection protection
- XSS prevention
- Secure password handling
- HTTPS recommended for production

## 🎥 Camera Requirements

- Device with camera (webcam, phone, tablet)
- HTTPS connection (or localhost for testing)
- Camera permissions granted in browser
- Good lighting conditions for best OCR results

## 📊 System Requirements

### Development
- Python 3.11+
- 500MB free disk space
- Modern web browser

### Docker Deployment
- Docker Desktop or Docker Engine
- 1GB RAM minimum
- 2GB free disk space
- Port 5000 available

## 🐛 Troubleshooting

### Docker not starting
- Ensure Docker Desktop is running
- Check port 5000 is not in use
- Verify Docker has sufficient resources

### Camera not working
- Use HTTPS or localhost
- Grant camera permissions
- Check if another app is using camera
- Try different browser

### Database issues
- Backup and delete parking.db
- Restart application
- Database will be recreated

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Built with ❤️ for smart parking management

## 🙏 Acknowledgments

- Flask framework
- Tesseract.js OCR engine
- Font Awesome icons
- Docker containerization

## 📞 Support

For issues and questions:
1. Check documentation files
2. Review troubleshooting section
3. Check Docker/Python logs
4. Verify camera permissions

---

## 🎉 Quick Start Commands

**Deploy with Docker:**
```bash
docker-compose up -d
```

**Access Application:**
- http://localhost:5000

**Admin Login:**
- http://localhost:5000/admin/login
- Username: admin / Password: admin123

**View Logs:**
```bash
docker-compose logs -f
```

**Stop Application:**
```bash
docker-compose down
```

---

**Ready to deploy? Run `deploy.bat` (Windows) or `./deploy.sh` (Linux/Mac)!**

🚗✨📷 Happy Parking!
