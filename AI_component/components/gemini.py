import logging
import os

import google.generativeai as genai

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Get env variable
GOOGLE_API_KEY = "AIzaSyBX5gH2mwWaNaq4u-h-b7l9RK1k0XRjTqk"
GEMINI_MODEL_NAME = "gemini-1.0-pro-latest"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')
chat = model.start_chat(history=[])
logging.info("Model gemini initialized")

def get_response(input_prompt: str, re_init: bool = False):
    if re_init:
        global chat
        chat = model.start_chat(history=[])
    chat.send_message(input_prompt)
    return chat.history[-1].parts[0].text

