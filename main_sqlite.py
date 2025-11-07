from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
import sqlite3
import os
import base64

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'canada$God7972#'

# Define total parking slots
TOTAL_SLOTS = 10

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'parking.db')

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            phone TEXT,
            password TEXT NOT NULL
        )
    ''')
    
    # Create reservations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            car_mark TEXT NOT NULL,
            car_number TEXT NOT NULL,
            slot INTEGER NOT NULL,
            parking_time TEXT,
            parking_date TEXT,
            hours INTEGER NOT NULL,
            status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Fetch booked slots
    cursor.execute('SELECT slot FROM reservations WHERE status = ?', ('booked',))
    booked_slots = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    
    empty_slots = [slot for slot in range(1, TOTAL_SLOTS + 1) if slot not in booked_slots]
    lastupdated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        'dashboard.html',
        username=session['username'],
        booked_slots=booked_slots,
        empty_slots=empty_slots,
        lastupdated=lastupdated,
        rate=20
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    success_msg = ''
    error_msg = ''

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        account = cursor.fetchone()
        conn.close()

        if account:
            session['loggedin'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error_msg = 'Incorrect username or password!'
    
    return render_template('login.html', success_msg=success_msg, error_msg=error_msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    success_msg = ''
    error_msg = ''

    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Check if username exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        if cursor.fetchone():
            error_msg = 'Username already exists!'
            conn.close()
        else:
            cursor.execute('INSERT INTO users (username, phone, password) VALUES (?, ?, ?)',
                         (username, phone, password))
            conn.commit()
            conn.close()
            success_msg = 'Signed up successfully! Please log in.'
            return render_template('login.html', success_msg=success_msg, error_msg=error_msg)

    return render_template('login.html', success_msg=success_msg, error_msg=error_msg)

@app.route('/reservation', methods=['GET'])
def reservation():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Fetch booked slots
    cursor.execute('SELECT slot FROM reservations WHERE status = ?', ('booked',))
    booked_slots = {row[0] for row in cursor.fetchall()}
    
    # Fetch all reservations for display
    cursor.execute('''SELECT username, car_mark, car_number, slot, parking_time, 
                      parking_date, hours, timestamp FROM reservations WHERE status = ?''', 
                   ('booked',))
    reservations = []
    for row in cursor.fetchall():
        reservations.append({
            'username': row[0],
            'carMark': row[1],
            'carNumber': row[2],
            'slot': row[3],
            'parkingTime': row[4],
            'parkingDate': row[5],
            'hours': row[6],
            'timestamp': row[7]
        })
    
    conn.close()
    
    empty_slots = [slot for slot in range(1, TOTAL_SLOTS + 1) if slot not in booked_slots]

    return render_template(
        'reservation.html',
        username=session['username'],
        empty_slots=empty_slots,
        reservations=reservations
    )

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    if 'loggedin' not in session:
        flash("Please log in to make a reservation.", "danger")
        return redirect(url_for('login'))

    username = session['username']
    car_mark = request.form.get('carMake')
    car_number = request.form.get('carNumber')
    slot = request.form.get('slot')
    parking_time = request.form.get('parkingTime')
    parking_date = request.form.get('parkingDate')
    hours = request.form.get('hours')

    # Validate input
    if not car_mark or not car_number or not slot or not parking_time or not parking_date or not hours:
        flash("Error: All fields are required!", "danger")
        return redirect(url_for('reservation'))

    try:
        slot = int(slot)
        hours = int(hours)
    except ValueError:
        flash("Error: Invalid input values!", "danger")
        return redirect(url_for('reservation'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if slot is already booked
    cursor.execute('SELECT * FROM reservations WHERE slot = ? AND status = ?', (slot, 'booked'))
    if cursor.fetchone():
        conn.close()
        flash("Error: Slot already booked!", "danger")
        return redirect(url_for('reservation'))

    # Insert reservation
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO reservations 
                      (username, car_mark, car_number, slot, parking_time, parking_date, hours, status, timestamp)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (username, car_mark, car_number, slot, parking_time, parking_date, hours, 'booked', timestamp))
    conn.commit()
    conn.close()

    flash("Reservation successful!", "success")
    return redirect(url_for('reservation'))

@app.route('/payment')
def payment():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    username = session['username']
    slot = request.args.get("slot")
    HOURLY_RATE = 20

    if not slot:
        flash("Invalid slot selection!", "danger")
        return redirect(url_for('dashboard'))

    try:
        slot = int(slot)
    except ValueError:
        flash("Invalid slot number!", "danger")
        return redirect(url_for('dashboard'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''SELECT hours, timestamp FROM reservations 
                      WHERE username = ? AND slot = ? AND status = ?''',
                   (username, slot, 'booked'))
    result = cursor.fetchone()
    conn.close()

    if not result:
        flash("No active reservation found for this slot!", "danger")
        return redirect(url_for('dashboard'))

    booked_hours = result[0]
    start_time_str = result[1]
    total_price = booked_hours * HOURLY_RATE

    return render_template(
        'payment.html',
        slot=slot,
        start_time=start_time_str,
        hours_parked=booked_hours,
        total_price=total_price
    )

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    username = session['username']
    slot = request.form.get('slot')
    total_price = request.form.get('total_price')

    if not slot or not total_price:
        flash("Invalid payment details!", "danger")
        return redirect(url_for('dashboard'))

    try:
        slot = int(slot)
    except ValueError:
        flash("Invalid slot number!", "danger")
        return redirect(url_for('dashboard'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete the reservation
    cursor.execute('DELETE FROM reservations WHERE username = ? AND slot = ? AND status = ?',
                   (username, slot, 'booked'))
    conn.commit()
    conn.close()

    flash(f"Payment successful for Slot {slot}. Amount Paid: ₹{total_price}", "success")
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error_msg = ''
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple admin credentials (in production, use database)
        if username == 'admin' and password == 'admin123':
            session['admin_loggedin'] = True
            session['admin_username'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            error_msg = 'Invalid admin credentials!'
    
    return render_template('admin_login.html', error_msg=error_msg)

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_loggedin' not in session:
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Fetch all reservations
    cursor.execute('''SELECT id, username, car_mark, car_number, slot, parking_time, 
                      parking_date, hours, status, timestamp FROM reservations 
                      WHERE status = ? ORDER BY timestamp DESC''', ('booked',))
    
    reservations = []
    for row in cursor.fetchall():
        reservations.append({
            'id': row[0],
            'username': row[1],
            'car_mark': row[2],
            'car_number': row[3],
            'slot': row[4],
            'parking_time': row[5],
            'parking_date': row[6],
            'hours': row[7],
            'status': row[8],
            'timestamp': row[9]
        })
    
    conn.close()
    
    return render_template('admin_dashboard.html', reservations=reservations)

@app.route('/admin/verify_plate', methods=['POST'])
def verify_plate():
    if 'admin_loggedin' not in session:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    try:
        data = request.get_json()
        plate_number = data.get('plate_number', '').strip().upper()
        
        print(f"DEBUG: Verifying plate number: {plate_number}")
        
        if not plate_number:
            return jsonify({'success': False, 'message': 'No plate number provided'})
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Check if plate number exists in reservations
        cursor.execute('''SELECT username, car_mark, car_number, slot, timestamp 
                          FROM reservations WHERE UPPER(REPLACE(car_number, ' ', '')) = UPPER(REPLACE(?, ' ', '')) AND status = ?''',
                       (plate_number, 'booked'))
        result = cursor.fetchone()
        
        print(f"DEBUG: Query result: {result}")
        
        conn.close()
        
        if result:
            return jsonify({
                'success': True,
                'authorized': True,
                'message': 'Vehicle Authorized!',
                'details': {
                    'username': result[0],
                    'car_mark': result[1],
                    'car_number': result[2],
                    'slot': result[3],
                    'timestamp': result[4]
                }
            })
        else:
            return jsonify({
                'success': True,
                'authorized': False,
                'message': 'Vehicle Not Authorized!',
                'details': None
            })
    except Exception as e:
        print(f"ERROR in verify_plate: {str(e)}")
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_loggedin', None)
    session.pop('admin_username', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    print("=" * 60)
    print("🚗 Smart Parking System - SQLite Version")
    print("=" * 60)
    print("✅ Database initialized successfully!")
    print("🌐 Server starting at: http://0.0.0.0:5000")
    print("📝 To register: http://localhost:5000/register")
    print("🔐 To login: http://localhost:5000/login")
    print("👨‍💼 Admin login: http://localhost:5000/admin/login")
    print("=" * 60)
    
    # Get debug mode from environment or default to False for production
    import os
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
