from typing import Union
import time
import logging

from fastapi import FastAPI
from pydantic import BaseModel

from AI_component.components.command_check import command_check

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

class Prompt(BaseModel):
    prompt_content:str
    first_time:bool


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
    return {
        "test": "ok"
    }
    