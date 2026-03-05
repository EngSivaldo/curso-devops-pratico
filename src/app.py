import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Conexão com o Banco de Dados usando a URL do docker-compose
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Criar a tabela de vendas se ela não existir
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS vendas (id serial PRIMARY KEY, produto varchar(100), data_venda timestamp DEFAULT CURRENT_TIMESTAMP);')
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def index():
    init_db()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM vendas;')
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template("index.html", mensagem=f"Total de vendas no banco: {total}")

@app.route("/comprar", methods=["POST"])
def comprar():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO vendas (produto) VALUES (%s)', ('Camiseta DevOps',))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("index.html", mensagem="✅ Venda salva no Banco de Dados!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
