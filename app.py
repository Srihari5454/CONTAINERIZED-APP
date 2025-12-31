import os
import sys
from flask import Flask, jsonify

app = Flask(__name__)

PORT = os.getenv("APP_PORT")

if not PORT:
    print("ERROR: APP_PORT environment variable not set", file=sys.stderr)
    sys.exit(1)

PORT = int(PORT)

@app.route("/")
def home():
    return jsonify(
        app_name="containerized-flask-app",
        port=PORT
    )

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    print(f"Starting app on port {PORT}")
    app.run(host="0.0.0.0", port=PORT)
