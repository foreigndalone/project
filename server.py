from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Разрешим CORS для простоты, чтобы можно было открыть HTML с диска
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/favorite", methods=["POST"])
def favorite():
    data = request.get_json(silent=True) or {}
    choice = data.get("choice")
    if not choice:
        return jsonify(ok=False, error="Missing 'choice'"), 400

    # тут можно сохранить в БД/файл/лог — пока просто печатаем
    print(f"[favorite] received: {choice}")

    return jsonify(ok=True, received=choice)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)