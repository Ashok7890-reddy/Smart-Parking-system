@echo off
echo ============================================================
echo   ParkFind Smart Parking System - Docker Deployment
echo ============================================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker is not running!
    echo.
    echo Please start Docker Desktop and try again.
    echo.
    pause
    exit /b 1
)

echo [1/5] Docker is running...
echo.

echo [2/5] Building Docker image...
docker-compose build
if %errorlevel% neq 0 (
    echo [ERROR] Build failed!
    pause
    exit /b 1
)
echo.

echo [3/5] Starting containers...
docker-compose up -d
if %errorlevel% neq 0 (
    echo [ERROR] Failed to start containers!
    pause
    exit /b 1
)
echo.

echo [4/5] Waiting for application to start...
timeout /t 5 /nobreak >nul
echo.

echo [5/5] Checking container status...
docker-compose ps
echo.

echo ============================================================
echo   Deployment Successful!
echo ============================================================
echo.
echo Application is running at:
echo   - Home: http://localhost:5000
echo   - User Login: http://localhost:5000/login
echo   - Admin Login: http://localhost:5000/admin/login
echo.
echo Admin Credentials:
echo   - Username: admin
echo   - Password: admin123
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down
echo.
pause
