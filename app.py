from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "Please provide a prompt"}), 400

    return jsonify({"response": f"Your query was: {prompt}"})

if __name__ == "__main__":
    app.run(debug=True)
