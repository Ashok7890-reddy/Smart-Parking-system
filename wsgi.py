from main_sqlite import app

# This is the WSGI application for production servers (Gunicorn, uWSGI, etc.)
# Gunicorn will use this 'app' object

if __name__ == "__main__":
    app.run()
