from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "Please provide a prompt"}), 400

    return jsonify({"response": f"Your query was: {prompt}"})

# Vercel requires this for deployment
def handler(event, context):
    return app(event, context)
