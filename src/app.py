import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM vendas;')
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template("index.html", mensagem=f"Total de vendas: {total}")

@app.route("/comprar", methods=["POST"])
def comprar():
    nome_cliente = request.form.get('nome_cliente') # Pega o nome do formulário
    conn = get_db_connection()
    cur = conn.cursor()
    # Agora inserimos o produto E o cliente
    cur.execute('INSERT INTO vendas (produto, cliente) VALUES (%s, %s)', 
                ('Camiseta DevOps', nome_cliente))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("index.html", mensagem=f"✅ Venda para {nome_cliente} salva!")

@app.route("/relatorio")
def relatorio():
    conn = get_db_connection()
    cur = conn.cursor()
    # Busca todas as vendas, da mais recente para a mais antiga
    cur.execute('SELECT id, produto, data_venda, cliente FROM vendas ORDER BY id DESC;')
    vendas_db = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("relatorio.html", vendas=vendas_db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)