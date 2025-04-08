from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your API key here
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if your key supports it
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
