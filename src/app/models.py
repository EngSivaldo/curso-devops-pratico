from . import get_db_connection

class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, nome, preco, estoque FROM produtos;')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Produto(*row) for row in rows]

class Venda:
    @staticmethod
    def registrar(produto_id, cliente_nome):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO vendas (produto, cliente) VALUES (%s, %s)',
                    (f"Produto ID: {produto_id}", cliente_nome))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def listar_relatorio():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, produto, data_venda, cliente FROM vendas ORDER BY id DESC;')
        vendas = cur.fetchall()
        cur.close()
        conn.close()
        return vendas

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM vendas;')
        total = cur.fetchone()[0]
        cur.close()
        conn.close()
        return total

class Usuario:
    @staticmethod
    def cadastrar(nome, email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome, email))
        conn.commit()
        cur.close()
        conn.close()
