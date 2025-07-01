from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "help": "I can answer questions about your account, payments, and more.",
    "contact": "You can reach support at support@example.com.",
    "default": "Sorry, I didn’t understand. Can you rephrase?"
}

@app.route("/")
def home():
    return render_template("index.html")  # Serve HTML

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    reply = responses.get(user_message, responses["default"])
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
