import streamlit as st
import pyperclip
from Translator import convert as Trans, explanation as Explain
import re

st.set_page_config(page_title="Real-Time Translator", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #121212;
            color: #f1f1f1;
        }

        html, body, [class*="css"] {
            background-color: #121212;
            color: #f1f1f1;
        }

        /* Title */
        h1 {
            color: #00f5ff;
            text-align: center;
            text-shadow: 0 0 5px #00f5ff, 0 0 10px #00f5ff;
        }

        /* Text areas */
        .stTextArea textarea {
            background-color: #1e1e1e !important;
            color: #f1f1f1 !important;
            border: 1px solid #00f5ff !important;
            border-radius: 8px;
            box-shadow: 0 0 10px #00f5ff33;
        }

        /* Select box */
        .stSelectbox > div {
            background-color: #1e1e1e !important;
            color: #f1f1f1 !important;
            border: 1px solid #ff00ff !important;
            border-radius: 6px;
            box-shadow: 0 0 8px #ff00ff33;
        }

        /* Buttons */
        .stButton > button {
            background-color: #9c27b0;
            color: #ffffff;
            border-radius: 10px;
            padding: 0.5em 1em;
            border: none;
            font-weight: bold;
            box-shadow: 0 0 12px #9c27b0, 0 0 6px #9c27b0;
            transition: 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #ba68c8;
            box-shadow: 0 0 16px #ba68c8, 0 0 10px #ba68c8;
        }

        /* Copy-to-clipboard feedback */
        .st-success {
            color: #00ffcc !important;
        }

        /* Spinner and alerts */
        .stSpinner, .stAlert {
            background-color: #2c2c2c !important;
            border-left: 5px solid #00f5ff !important;
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
target_lang = target_lang_name  

translated_text = ""

if st.button("Translate"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating with auto-detection..."):
            try:
                if mode == "Just Translate":
                    translated_text = Trans(text_input, target_lang)
                else:
                    translated_text = Explain(text_input, target_lang)
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

