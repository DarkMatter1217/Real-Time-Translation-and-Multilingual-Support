from google import generativeai as genai
import dotenv
dotenv.load_dotenv()
import os
genai.configure(api_key=os.getenv("API_KEY"))  

def convert(i, target_language):
    prompt = f"Convert {i} to {target_language}, Only give translation, no other text or explanation."
    model = genai.GenerativeModel("gemini-2.0-flash")  
    response = model.generate_content(prompt)
    return response.text

def explanation(i, target_language):
    prompt = f"""Convert {i} to {target_language}. First give translation in bold, then explain the thought process of conversion in detail."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

