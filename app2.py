import streamlit as st
import pyperclip
from Translator import convert as Trans, explanation as Explain
import re

st.set_page_config(page_title="Real-Time Translator", layout="centered")

# Theme Toggle
dark_mode = st.sidebar.checkbox("\ud83c\udf19 Enable Dark Theme")

# Apply CSS based on toggle
if dark_mode:
    st.markdown("""
    <style>
        body, .main {
            background-color: #0e0e0e;
            color: #ccffcc;
        }
        h1 {
            color: #00ff88 !important;
            font-size: 2.5rem !important;
            font-weight: 900 !important;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 2px solid #00ff88;
            padding-bottom: 10px;
            margin-bottom: 30px;
            text-shadow: 0 0 5px #00ff88, 0 0 10px #00ff88, 0 0 15px #00cc66;
        }
        .stTextArea textarea, .stSelectbox div, .stButton button {
            background-color: #1a1a1a !important;
            color: #d9ffd9 !important;
            border: 1px solid #00cc66 !important;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .stTextArea textarea:hover, .stSelectbox div:hover, .stButton button:hover {
            transform: scale(1.03);
            box-shadow: 0 0 8px #00ff88;
        }
        .stButton > button {
            background-color: #00cc66 !important;
            color: white !important;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #00994d !important;
            transform: scale(1.05);
            box-shadow: 0 0 10px #00ff88;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        body, .main {
            background-color: #e6f7ff;
            color: #003333;
        }
        h1 {
            color: #00aa88 !important;
            font-size: 2.5rem !important;
            font-weight: 900 !important;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 2px solid #00aa88;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        .stTextArea textarea, .stSelectbox div, .stButton button {
            background-color: #f2fefd !important;
            color: #003333 !important;
            border: 1px solid #00b386 !important;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .stTextArea textarea:hover, .stSelectbox div:hover, .stButton button:hover {
            transform: scale(1.03);
            box-shadow: 0 0 8px #00b386;
        }
        .stButton > button {
            background-color: #00b386 !important;
            color: white !important;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #009973 !important;
            transform: scale(1.05);
            box-shadow: 0 0 10px #00b386;
        }
    </style>
    """, unsafe_allow_html=True)

# UI Starts Here
st.markdown("<h1>\ud83c\udf0d Real-Time Translator</h1>", unsafe_allow_html=True)

language_dict = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-cn', 'Chinese (Traditional)': 'zh-tw', 'Japanese': 'ja',
    'Korean': 'ko', 'Arabic': 'ar', 'Russian': 'ru', 'Italian': 'it', 'Portuguese': 'pt',
    'Bengali': 'bn', 'Urdu': 'ur', 'Turkish': 'tr', 'Tamil': 'ta', 'Telugu': 'te',
    'Gujarati': 'gu', 'Punjabi': 'pa'
}

text_input = st.text_area("Enter text", max_chars=1000, height=150)
mode = st.selectbox("Select Mode", ["Just Translate", "Detailed Explanation"])
target_lang_name = st.selectbox("Translate To", list(language_dict.keys()), index=0)
target_lang = language_dict[target_lang_name]

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
    clean_text = clean_text.replace('\n\n', '\n').strip()

    st.text_area("Translation Output", value=clean_text, height=250, key="output")
    if st.button("\ud83d\udccb Copy to Clipboard"):
        pyperclip.copy(clean_text)
        st.success("Copied to clipboard!")
