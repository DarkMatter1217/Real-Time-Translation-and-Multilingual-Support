from google import generativeai as genai
import dotenv
dotenv.load_dotenv()
import os
genai.configure(api_key=os.getenv("API_KEY"))  

def convert(i, target_language):
    prompt = f"Translate {i} to {target_language} return only the best matching translation without any additional information"
    model = genai.GenerativeModel("gemini-2.0-flash")  
    response = model.generate_content(prompt)
    return response.text

def explanation(i, target_language):
    prompt = f"""Translate {i} to {target_language} also explain the translation step by step """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

