from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Olá, Sival!</h1><p>Seu e-commerce de teste está ON no Docker!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
