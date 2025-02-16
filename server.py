import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get API key from environment variable (Vercel will provide it)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

@app.route("/api/generate", methods=["POST"])
def generate_response():
    data = request.get_json()
    user_prompt = data.get("prompt")

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    request_body = {
        "contents": [{"parts": [{"text": user_prompt}]}]
    }

    try:
        response = requests.post(GEMINI_URL, json=request_body, headers={"Content-Type": "application/json"})
        response_data = response.json()

        if "candidates" in response_data:
            ai_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"response": ai_response})
        else:
            return jsonify({"error": "Invalid response from Gemini API"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Flask API for Gemini AI is running!"

if __name__ == "__main__":
    app.run(debug=True)
