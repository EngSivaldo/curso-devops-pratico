import os
from flask import Flask
import psycopg2

def create_app():
    app = Flask(__name__)
    
    # Configuração do Banco vinda do Ambiente (Docker)
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

    from . import routes
    app.register_blueprint(routes.bp)

    return app

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn
