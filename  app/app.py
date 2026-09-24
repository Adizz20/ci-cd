from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Session 17 DevSecOps",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!"
    })


@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    number1 = data.get("number1")
    number2 = data.get("number2")

    result = number1 + number2

    return jsonify({
        "number1": number1,
        "number2": number2,
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)