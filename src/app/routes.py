from flask import Blueprint, render_template, request, redirect, url_for
from . import get_db_connection

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM vendas;')
    total_vendas = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template('index.html', total_vendas=total_vendas)

@bp.route('/comprar', methods=['POST'])
def comprar():
    nome_cliente = request.form.get('nome_cliente')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO vendas (produto, cliente) VALUES (%s, %s)',
                ('Camiseta DevOps', nome_cliente))
    conn.commit()
    cur.close()
    conn.close()
    return f"<h1>✅ Venda para {nome_cliente} salva!</h1><a href='/'>Voltar</a>"

@bp.route('/relatorio')
def relatorio():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, produto, data_venda, cliente FROM vendas ORDER BY id DESC;')
    vendas_db = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('relatorio.html', vendas=vendas_db)
