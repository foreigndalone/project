from flask import Flask, request

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    gender = request.form.get("gender")
    print(f"Привет, {name}! Ты указал пол: {gender}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)