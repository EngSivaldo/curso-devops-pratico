FROM python:3.9-slim
# Instala dependências do sistema para o banco de dados
RUN apt-get update && apt-get install -y libpq-dev gcc
WORKDIR /app
RUN pip install flask psycopg2-binary
COPY src/ /app/
EXPOSE 5000
CMD ["python", "app.py"]
