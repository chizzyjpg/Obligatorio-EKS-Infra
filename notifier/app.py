from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json(silent=True) or {}
    print("[NOTIFIER] Mensaje recibido:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
