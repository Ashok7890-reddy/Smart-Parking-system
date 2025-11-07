# 🚗 ParkFind - Smart Parking System

A modern, feature-rich smart parking management system with **live camera-based number plate recognition**, built with Flask and ready for cloud deployment.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌐 Live Demo

**Coming Soon:** Deploy to see it live!

## ✨ Key Features

### 👥 User Features
- **Modern Responsive UI** - Beautiful gradient theme, works on all devices
- **User Authentication** - Secure registration and login
- **Real-time Dashboard** - Live parking slot availability
- **Smart Reservations** - Easy booking with date/time selection
- **Payment System** - Integrated billing (₹20/hour)
- **Reservation History** - Track all bookings

### 🛡️ Admin Features
- **Admin Portal** - Separate management interface
- **Live Camera Feed** - Real-time video from device camera
- **OCR Technology** - Automatic number plate recognition (Tesseract.js)
- **Instant Verification** - Real-time authorization checks
- **Visual Feedback** - Color-coded results (Green/Red)
- **Audio Alerts** - Beep sounds for success/failure
- **Reservations Monitor** - View all active bookings

### 📷 Number Plate Recognition
- Live camera access from any device
- Automatic OCR detection
- Pattern matching and validation
- Auto-fill detected plates
- Manual entry fallback
- Works on desktop, mobile, and tablets

## 🚀 Quick Deploy (5 Minutes)

### Deploy to Render.com (Recommended - FREE)

1. **Sign up:** https://render.com (use GitHub)
2. **Create Web Service** → Connect repository
3. **Configure:**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn wsgi:app
   ```
4. **Add Disk:** Mount path `/app/data` (1GB)
5. **Deploy!**

**Detailed Guide:** See [DEPLOY_NOW.md](DEPLOY_NOW.md)

## 💻 Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Clone repository
git clone https://github.com/Ashok7890-reddy/Smart-Parking-system.git
cd Smart-Parking-system

# Install dependencies
pip install -r requirements.txt

# Run application
python main_sqlite.py
```

### Access
- **Home:** http://127.0.0.1:5000
- **Admin:** http://127.0.0.1:5000/admin/login
- **Credentials:** admin / admin123

## 🐳 Docker Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Or manually
docker build -t parkfind .
docker run -p 5000:5000 parkfind
```

**Guide:** See [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)

## 📁 Project Structure

```
Smart-Parking-system/
├── templates/              # HTML templates
│   ├── index.html         # Home page
│   ├── login.html         # User auth
│   ├── dashboard.html     # User dashboard
│   ├── reservation.html   # Booking page
│   ├── payment.html       # Payment page
│   ├── admin_login.html   # Admin auth
│   └── admin_dashboard.html # Admin panel with camera
├── static/                # CSS, JS, images, fonts
├── main_sqlite.py         # Main Flask application
├── wsgi.py                # WSGI entry point
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose config
├── render.yaml            # Render.com config
└── README.md              # This file
```

## 🛠️ Technology Stack

**Backend:**
- Flask 3.0.2 - Web framework
- SQLite - Database
- Gunicorn - Production server

**Frontend:**
- HTML5, CSS3, JavaScript
- Tesseract.js - OCR engine
- Font Awesome - Icons

**Deployment:**
- Docker & Docker Compose
- Render.com / Railway.app ready

## 🔐 Default Credentials

**Admin Login:**
- URL: `/admin/login`
- Username: `admin`
- Password: `admin123`

**⚠️ Change these in production!**

## 📚 Documentation

- **[DEPLOY_NOW.md](DEPLOY_NOW.md)** - Quick deployment guide (5 min)
- **[PRODUCTION_DEPLOYMENT.md](PRODUCTION_DEPLOYMENT.md)** - Gunicorn configuration
- **[DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)** - Docker guide
- **[CAMERA_GUIDE.md](CAMERA_GUIDE.md)** - Camera feature docs
- **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - Admin dashboard guide
- **[QUICK_START.md](QUICK_START.md)** - Development setup

## 🎯 Use Cases

### For Parking Operators
- Monitor real-time occupancy
- Verify vehicle authorization
- Quick plate scanning at entry
- Track reservations and payments

### For Drivers
- Find available spots
- Reserve in advance
- View pricing
- Secure payments

### For Security
- Scan plates with camera
- Instant authorization
- Audio/visual feedback
- Direct to assigned slots

## 🌟 Features Highlight

✨ **Beautiful UI** - Modern gradient design
📷 **Live Camera** - Real-time plate recognition
🤖 **OCR Technology** - Automatic detection
⚡ **Fast** - Quick response times
📱 **Responsive** - Works on all devices
🔒 **Secure** - Protected authentication
💰 **Payment** - Integrated billing
📊 **Real-time** - Live updates
🐳 **Docker Ready** - Easy deployment
☁️ **Cloud Ready** - Deploy anywhere

## 🚀 Deployment Options

| Platform | Free Tier | Database | Recommended |
|----------|-----------|----------|-------------|
| **Render.com** | ✅ Yes | ✅ Persistent | ✅ **Best** |
| **Railway.app** | ✅ Yes | ✅ Persistent | ✅ Good |
| **Docker** | ✅ Yes | ✅ Persistent | ✅ Local |
| Vercel | ✅ Yes | ❌ Resets | ❌ No |

## 📱 Browser Support

- ✅ Chrome (recommended for camera)
- ✅ Firefox
- ✅ Edge
- ✅ Safari
- ✅ Mobile browsers

## 🔧 Configuration

### Environment Variables

```bash
FLASK_ENV=production
PORT=5000
SECRET_KEY=your-secret-key
```

### Database

SQLite database auto-created at:
- Local: `./parking.db`
- Render: `/app/data/parking.db`

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - feel free to use for any purpose

## 👨‍💻 Author

**Ashok Reddy**
- GitHub: [@Ashok7890-reddy](https://github.com/Ashok7890-reddy)
- Repository: [Smart-Parking-system](https://github.com/Ashok7890-reddy/Smart-Parking-system)

## 🙏 Acknowledgments

- Flask framework
- Tesseract.js OCR
- Font Awesome icons
- Render.com hosting

## 📞 Support

- 📖 Check documentation files
- 🐛 Report issues on GitHub
- 💬 Discussions welcome

---

## 🎉 Quick Commands

**Local Development:**
```bash
python main_sqlite.py
```

**Docker:**
```bash
docker-compose up -d
```

**Deploy to Render:**
```bash
# Push to GitHub, then connect on Render.com
git push origin main
```

---

**⭐ Star this repo if you find it useful!**

**🚀 Ready to deploy?** See [DEPLOY_NOW.md](DEPLOY_NOW.md)

**📷 Camera not working?** See [CAMERA_GUIDE.md](CAMERA_GUIDE.md)

**🛡️ Admin help?** See [ADMIN_GUIDE.md](ADMIN_GUIDE.md)
