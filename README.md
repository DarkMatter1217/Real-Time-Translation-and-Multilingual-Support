# Real-Time-Translation-and-Multilingual-Support
## https://translator001.streamlit.app/

A Streamlit-based application that provides on-the-fly translation of user content and supports multilingual interactions across various input formats.

---

## 🚀 Features

* **Live Translation**: Translates text, documents, or chat messages in real time between any two supported languages.
* **Multilingual Chat Interface**: Users can converse in their native language; the app automatically translates both sides of the conversation.
* **Document Translation**: Upload files (PDF, DOCX, TXT) to translate entire documents preserving basic formatting.
* **Speech-to-Text & Text-to-Speech**: Record voice input for translation and listen to translated output via TTS.
* **Language Detection**: Automatically identifies the source language to streamline user experience.
* **Customizable Output**: Choose formal or informal tone and specify regional dialects (e.g., en-US vs. en-GB).

---

## 📦 Tech Stack

* **Framework**: Streamlit for rapid development of the web UI and layout.
* **LLM Orchestration**: LangChain to manage prompt flows for translation tasks.
* **Translation API**: Google Translate API (via `google-cloud-translate`) and/or OpenAI’s translation endpoints.
* **Speech Processing**: `speechrecognition` for STT, `gTTS` for TTS playback.
* **Document Parsing**: PyPDF2 & python-docx for extracting text from uploaded files.
* **Embeddings & Caching**: sentence-transformers for semantic caching of previously translated segments backed by FAISS.
* **Storage**: SQLite with SQLAlchemy to log user sessions, translation history, and preferences.
* **Environment**: python-dotenv & Streamlit `secrets.toml` for API keys and config.
* **Utilities**: pandas & NumPy for data manipulation; python-dateutil for timestamp normalization.

---

## 💡 Architecture Overview

1. **User Input**: Text, document, or voice input is captured in the Streamlit interface.
2. **Language Detection**: Source language auto-detected; user can override if desired.
3. **Preprocessing**: Text extracted (from files or speech) and chunked for translation.
4. **Translation Chain**: LangChain routes chunks to the selected translation API with user-specified tone.
5. **Postprocessing**: Chunks reassembled; formatting from original document is preserved as much as possible.
6. **TTS Output**: If enabled, translated text is converted to speech for playback.
7. **Caching**: Previously translated segments stored as embeddings and retrieved via FAISS to reduce API calls.
8. **Persistence**: All sessions, translations, and user preferences are stored in SQLite for later review.

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/DarkMatter1217/Real-Time-Translation-and-Multilingual-Support.git
cd Real-Time-Translation-and-Multilingual-Support

# Create virtual environment
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Configuration

1. Create a `.env` file at project root:

   ```ini
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

---

## 🛠️ Contributing

1. Fork the repository and create a feature branch.
2. Install dependencies and run tests where applicable.
3. Submit a Pull Request with clear description of your changes.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Enjoy seamless multilingual communication!*
