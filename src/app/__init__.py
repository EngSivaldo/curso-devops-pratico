import os
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2


metrics = PrometheusMetrics.for_app_factory() # Prepara para o padrão Factory
def create_app():
    app = Flask(__name__)
    
    # Configuração do Banco vinda do Ambiente (Docker)
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

    from . import routes
    app.register_blueprint(routes.bp)
    metrics.init_app(app) # Inicializa as métricas aqui!

    return app

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn
