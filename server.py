from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # разрешает кросс-доменные запросы

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name")
    gender = data.get("gender")
    print(f"Привет, {name}! Ты указал пол: {gender}")
    return f"Привет, {name}! Ты указал пол: {gender}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)