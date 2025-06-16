import streamlit as st
import pyperclip
from Translator import convert as Trans, explanation as Explain
import re

st.set_page_config(page_title="Real-Time Translator", layout="centered")

st.markdown("""
    <style>
        body { background-color: #1e1e1e; color: #f1f1f1; }
        .stTextArea textarea, .stSelectbox div, .stButton button, .stMarkdown p {
            background-color: #2e2e2e; color: white;
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

