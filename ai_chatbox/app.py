from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from characters.utils import load_character_yaml, build_system_prompt

app = Flask(__name__)
CORS(app)

# 🔑 Replace with your OpenRouter API key
API_KEY = "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"  
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct"  # or any supported model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    character_name = data.get("character", "liora")

    try:
        # Load character info
        char_data = load_character_yaml(character_name)
        system_prompt = build_system_prompt(char_data)

        # Call OpenRouter
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        bot_reply = response.json()['choices'][0]['message']['content']

        return jsonify({"response": bot_reply})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"response": f"Bot: Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
