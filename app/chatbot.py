import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# Simple in-memory chat history
chat_history = []

def get_response(user_input, persona_prompt, chat_history):
    # Combine persona and user input
    prompt = f"{persona_prompt}\nUser: {user_input}\nAssistant:"
    # Optionally, add chat history for context
    if chat_history:
        history_text = "\n".join([f"User: {q}\nAssistant: {a}" for q, a in chat_history])
        prompt = f"{history_text}\n{prompt}"
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, 'text') else str(response) 