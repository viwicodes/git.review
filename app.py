from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "GitLab AI MR Reviewer is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return jsonify({"message": "No data received"}), 400

    # Process webhook data (e.g., check for merge request event)
    print(json.dumps(data, indent=4, sort_keys=True))
    print(data)
    return jsonify({"message": "Webhook received", "data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)