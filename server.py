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

# Vercel requires this to wrap Flask in a handler for serverless deployment
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

# Vercel uses "server.py" instead of "app.py"
if __name__ == "__main__":
    app.run(debug=True)
