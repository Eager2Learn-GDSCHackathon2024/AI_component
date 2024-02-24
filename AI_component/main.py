from typing import Union
import time
import logging

from fastapi import FastAPI
from pydantic import BaseModel

from AI_component.components.command_check import command_check
from AI_component.components.gemini import get_response
from AI_component.components.lesson_introduction import get_introduce_transcript
from AI_component.firebase.firebase import get_outline

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

class Prompt(BaseModel):
    prompt_content:str
    first_time:bool
    outline: dict
    user_info: dict


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Post from prompt text (pre-processed in JS backend)
@app.post("/prompt")
async def prompt_processing(prompt: Prompt = None):
    if prompt is None:
        return {
            "error": "Prompt is None"
        }
    # Detect action/prompt
    start = time.time()
    detect_action = command_check(prompt.prompt_content)
    logging.info(f"Detect action time: {time.time() - start}")
    if detect_action != -1:
        return {
            "type": "action",
            "action_type": detect_action
        }

    logging.info("Handling the prompt...")
    if prompt.first_time:
        start = time.time()
        response = handle_first_time(prompt)
        logging.info(f"handle_first_time time: {time.time() - start}")
        return {
            "type": "prompt",
            "outline": get_outline(prompt),
            "result": response
        }
    
    # RAG-like process

    # Get response
    response = get_response(prompt.prompt_content)

    # Return the result
    return {
        "type": "prompt",
        "outline": prompt.outline,
        "result": response
    }
    
def handle_first_time(prompt):
    # response = get_response(f"Hãy trả về cho tôi một đoạn văn giống như đoạn văn này: {get_introduce_transcript(prompt)}. Thông tin người dùng là {str(prompt.user_info)}")
    # Do other first-time things

    return get_introduce_transcript(prompt)
