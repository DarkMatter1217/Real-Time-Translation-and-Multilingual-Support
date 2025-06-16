from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for JS in frontend

translator = Translator()

@app.route("/")
def home():
    return render_template("translation.html")  # Serve HTML UI

@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    source_lang = data.get("sourceLang", "en")
    target_lang = data.get("targetLang", "hi")

    if not text.strip():
        return jsonify({"error": "Empty text"}), 400

    try:
        result = translator.translate(text, src=source_lang.lower(), dest=target_lang.lower())
        return jsonify({"translatedText": result.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
