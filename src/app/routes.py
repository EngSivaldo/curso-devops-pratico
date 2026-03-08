from flask import Blueprint, render_template, request, redirect, url_for
from .models import Produto, Venda, Usuario

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', 
                           total_vendas=Venda.contar_total(), 
                           produtos=Produto.listar_todos())

@bp.route('/comprar', methods=['POST'])
def comprar():
    Venda.registrar(request.form.get('produto_id'), request.form.get('nome_cliente'))
    return redirect(url_for('main.index'))

@bp.route('/relatorio')
def relatorio():
    return render_template('relatorio.html', vendas=Venda.listar_relatorio())

@bp.route('/cadastro')
def tela_cadastro():
    return render_template('cadastro.html')

@bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        Usuario.cadastrar(request.form.get('nome'), request.form.get('email'))
        return redirect(url_for('main.index'))
    except Exception:
        return "Erro ao cadastrar. E-mail possivelmente já existe.", 400