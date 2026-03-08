FROM python:3.9-slim

# Instala dependências do sistema para o Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

# 1. Copia o arquivo de requisitos primeiro
COPY requirements.txt .

# 2. Comando CORRETO: Instala o que estiver no arquivo!
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código fonte
COPY src/ /app/

CMD ["python", "wsgi.py"]