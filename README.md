# Curso DevOps Prático - E-commerce com Docker

Este projeto é um servidor web simples utilizando **Python** e **Flask**, totalmente containerizado com **Docker**.

## 🚀 Como rodar o projeto

Certifique-se de ter o Docker e o Docker Compose instalados.

1. Clone o repositório:
   ```bash
   git clone https://github.com/EngSivaldo/curso-devops-pratico.git
   ```

2. Entre na pasta:
   ```bash
   cd curso-devops-pratico
   ```

3. Suba o ambiente:
   ```bash
   docker compose up --build
   ```

4. Acesse no seu navegador:
   [http://localhost:8080](http://localhost:8080)

## 🛠️ Tecnologias Utilizadas
* **Docker**: Para isolamento do ambiente.
* **Flask**: Framework web em Python.
* **GitHub Actions**: Para integração contínua (CI).


curso-devops/
├── docker-compose.yml     # Orquestrador (Infra)
├── Dockerfile             # Receita da Imagem (App)
├── nginx/
│   └── nginx.conf         # Configuração do Proxy (Rede)
└── src/                   # Código Fonte
    ├── wsgi.py            # Ponto de entrada (Entrypoint)
    └── app/               # O pacote da aplicação
        ├── __init__.py    # A Fábrica (Factory)
        ├── routes.py      # As rotas (Lógica)
        └── templates/     # A cara do site (HTML)