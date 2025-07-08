# Real-Time-Translation-and-Multilingual-Support
## https://translator001.streamlit.app/

A dual-interface translation application offering:

* **Flask Web UI** using `googletrans` for instant text translation via a minimal HTML/JavaScript frontend.
* **Streamlit App** leveraging Google’s Gemini API (`google-generativeai`) for advanced translation and step-by-step explanations.

---

## 🗂 Repository Structure

```
├── app.py                # Flask backend serving translation UI
├── Translator.py         # Wrapper around Google Generative AI for Streamlit app
├── app2.py               # Streamlit frontend for real-time translation & explanations
├── templates/            # HTML templates for Flask app
│   └── translation.html
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API_KEY)
└── README.md             # This file
```

---

## ⚡️ Key Features

1. **Flask Translation UI** (`app.py` + `templates/translation.html`)

   * Simple HTML interface to enter text and select source/target languages.
   * Uses `googletrans` (community edition) for free, offline language translation.
   * AJAX-based POST to `/api/translate` with JSON responses.

2. **Streamlit Translator** (`app2.py` + `Translator.py`)

   * Sidebar toggle for light/dark themes.
   * Two modes: **Just Translate** and **Detailed Explanation**.
   * Supports 20+ languages via `Translator.convert` and `Translator.explanation`.
   * Auto language detection and seamless copy-to-clipboard functionality.

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DarkMatter1217/Real-Time-Translation-and-Multilingual-Support.git
   cd Real-Time-Translation-and-Multilingual-Support
   ```

2. **Create & activate virtual environment**

   ```bash
   python3 -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   * Create a `.env` file in the project root:

     ```ini
     API_KEY=<your_google_api_key>
     ```
   * This key is used by `Translator.py` for Gemini-based translation/explanation.

---

## 🏃‍♂️ Running the Apps

### 1. Flask Web UI

```bash
# Start Flask server
env FLASK_APP=app.py flask run
```

* Open your browser at `http://localhost:5000`
* Enter text, choose languages, and click **Translate**

### 2. Streamlit Translator

```bash
streamlit run app2.py
```

* Use the sidebar to enable Dark Mode
* Enter text, select **Mode** (Translate or Explain), and target language
* Click **Translate** and view/copy the output

---

## 🧩 Technologies

| Component          | Technology                        |
| ------------------ | --------------------------------- |
| Flask Web Server   | Flask, Flask-CORS                 |
| Translation API    | googletrans (v4.0.0-rc1)          |
| Streamlit Frontend | Streamlit, Pyperclip              |
| Generative AI      | Google Generative AI (Gemini API) |
| Environment        | python-dotenv                     |

---

## 🤝 Contributing

* Fork this repository
* Create a feature branch (`git checkout -b feature/XYZ`)
* Commit your changes and push (`git push origin feature/XYZ`)
* Open a Pull Request detailing your improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
   GOOGLE_API_KEY=<your_google_cloud_key>
   OPENAI_API_KEY=<your_openai_key>        # if using OpenAI endpoints
   ```
2. Add any additional settings to `.streamlit/secrets.toml` if needed.

---

## 📈 Usage

```bash
streamlit run app.py
```

* Open [http://localhost:8501](http://localhost:8501) in your browser.
* Select input mode: Text, Document, or Voice.
* Choose source and target languages (auto-detect available).
* Configure tone and dialect.
* View translated output; enable TTS for audio playback.


