import streamlit as st
import pyperclip
from Translator import convert as Trans, explanation as Explain
import re

st.set_page_config(page_title="Real-Time Translator", layout="centered")

dark_mode = st.sidebar.checkbox("Enable Dark Theme")

st.markdown(f"""
<style>
    html, body, .main, [data-testid="stAppViewContainer"] {{
        background-color: {"#0e0e0e" if dark_mode else "#e6f7ff"} !important;
        color: {"#ccffcc" if dark_mode else "#003333"} !important;
        transition: background-color 0.5s ease, color 0.5s ease;
    }}

    h1 {{
        text-align: center;
        color: {"#66ffcc" if dark_mode else "#00664d"};
        font-size: 2.5rem;
        font-weight: 900;
        text-transform: uppercase;
        border-bottom: 3px solid {"#00cc66" if dark_mode else "#00b386"};
        padding-bottom: 10px;
        margin-bottom: 30px;
        text-shadow: 0 0 8px {"#00ff88" if dark_mode else "transparent"};
    }}

    .stTextArea textarea {{
        width: 100%;
        font-size: 1rem;
        padding: 12px;
        border-radius: 8px;
        background-color: {"#1a1a1a" if dark_mode else "#f2fefd"} !important;
        color: {"#d9ffd9" if dark_mode else "#003333"} !important;
        border: 1px solid {"#00cc66" if dark_mode else "#00b386"};
        transition: all 0.3s ease;
    }}

    .stTextArea textarea:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 8px {"#00ff88" if dark_mode else "#00b386"};
    }}

    .stSelectbox > div[data-baseweb="select"] {{
        background-color: {"#1a1a1a" if dark_mode else "#f2fefd"} !important;
        color: {"#d9ffd9" if dark_mode else "#003333"} !important;
        border: 1px solid {"#00cc66" if dark_mode else "#00b386"} !important;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}

    .stSelectbox > div[data-baseweb="select"]:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 8px {"#00ff88" if dark_mode else "#00b386"};
    }}

    .stButton > button {{
        background-color: {"#00cc66" if dark_mode else "#00b386"} !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px;
        transition: all 0.3s ease;
    }}

    .stButton > button:hover {{
        background-color: {"#00994d" if dark_mode else "#009973"} !important;
        transform: scale(1.05);
        box-shadow: 0 0 10px {"#00ff88" if dark_mode else "#00b386"};
    }}

    .footer {{
        text-align: center;
        font-size: 0.9rem;
        margin-top: 20px;
        color: {"#88ffcc" if dark_mode else "#4d6666"};
    }}

    /* Dropdown menu popup */
    [data-baseweb="popover"] {{
        background-color: {"#1a1a1a" if dark_mode else "#ffffff"} !important;
        color: {"#d9ffd9" if dark_mode else "#003333"} !important;
        border: 1px solid {"#00cc66" if dark_mode else "#00b386"} !important;
        border-radius: 8px;
    }}

    [data-baseweb="popover"] div[role="option"] {{
        background-color: {"#1a1a1a" if dark_mode else "#ffffff"} !important;
        color: {"#d9ffd9" if dark_mode else "#003333"} !important;
    }}

    [data-baseweb="popover"] div[role="option"]:hover {{
        background-color: {"#005c3b" if dark_mode else "#e0f5f0"} !important;
    }}

    /* Label fix */
    label, .stSelectbox label {{
        color: {"#d9ffd9" if dark_mode else "#003333"} !important;
        font-weight: 600;
    }}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🌍 Real-Time Translator</h1>", unsafe_allow_html=True)

# Languages
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
                    translated_text = Trans(text_input, target_lang_name)
                else:
                    translated_text = Explain(text_input, target_lang_name)
                st.success("Translation Complete")
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")

if translated_text:
    clean_text = re.sub(r'\*\*(.*?)\*\*', r'\1', translated_text)
    clean_text = re.sub(r'\*(.*?)\*', r'\1', clean_text)
    clean_text = clean_text.replace('\n\n', '\n').strip()

    st.text_area("Translation Output", value=clean_text, height=250, key="output")
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(clean_text)
        st.success("Copied to clipboard!")

