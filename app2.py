import streamlit as st
import pyperclip
from Translator import convert as Trans, explanation as Explain
import re

st.set_page_config(page_title="Real-Time Translator", layout="centered")
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&family=Poppins:wght@300;500;700&display=swap');

        /* Background Animation */
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: white;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Main container */
        .main {
            padding: 2rem;
        }

        /* Title */
        h1 {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            font-size: 3em;
            color: #00ffe1;
            text-shadow: 0 0 10px #00ffe1, 0 0 20px #00ffe1;
            animation: fadeInDown 1s ease-out;
        }

        /* Input Areas */
        .stTextArea textarea {
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid #00ffe1;
            border-radius: 12px;
            color: #ffffff;
            padding: 1rem;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(8px);
            font-size: 1rem;
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Select boxes */
        .stSelectbox > div {
            background: rgba(255, 255, 255, 0.07);
            border-radius: 10px;
            border: 2px solid #ff00ff;
            color: white;
            box-shadow: 0 0 10px #ff00ff33;
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 1rem;
            font-weight: 600;
            box-shadow: 0 0 20px #ff416c88;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            animation: fadeIn 1.2s ease-in-out;
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #ff4b2b, #ff416c);
            transform: scale(1.05);
            box-shadow: 0 0 25px #ff416caa;
        }

        /* Messages */
        .st-success {
            color: #00ffcc !important;
            font-weight: bold;
        }

        .stAlert, .stSpinner {
            background-color: rgba(0, 0, 0, 0.5) !important;
            border-left: 5px solid #00ffe1;
        }

        textarea[readonly] {
            background-color: rgba(255, 255, 255, 0.08) !important;
            border: 1px dashed #00ffcc;
            border-radius: 10px;
        }

        /* Animations */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInDown {
            0% { opacity: 0; transform: translateY(-30px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Footer */
        .footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.8rem;
            color: #888;
            font-style: italic;
        }
    </style>
""", unsafe_allow_html=True)




st.title("🌍 Real-Time Translator")

language_dict = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Arabic': 'ar',
    'Russian': 'ru',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Bengali': 'bn',
    'Urdu': 'ur',
    'Turkish': 'tr',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Gujarati': 'gu',
    'Punjabi': 'pa'
}

text_input = st.text_area("Enter text", max_chars=1000, height=150)

mode = st.selectbox("Select Mode", ["Just Translate", "Detailed Explanation"])

target_lang_name = st.selectbox("Translate To", list(language_dict.keys()), index=0)

translated_text = ""

if st.button("Translate"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating with auto-detection..."):
            try:
                if mode == "Just Translate":
                    translated_text = Trans(text_input, target_lang_name)
                else:
                    translated_text = Explain(text_input, target_lang_name)
                st.success("Translation Complete")
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")


if translated_text:
    clean_text = re.sub(r'\*\*(.*?)\*\*', r'\1', translated_text)
    clean_text = re.sub(r'\*(.*?)\*', r'\1', clean_text)           
    clean_text = clean_text.replace('\n\n', '\n')                  
    clean_text = clean_text.strip()

    st.text_area("Translation Output", value=clean_text, height=250, key="output")
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(clean_text)
        st.success("Copied to clipboard!")

