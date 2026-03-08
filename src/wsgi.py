from app import create_app

app = create_app()

if __name__ == "__main__":
        # No seu arquivo src/app/__init__.py ou wsgi.py
    app.run(host='0.0.0.0', port=5000)  # nosec
