from typing import Union
import time
import logging

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

import AI_component.firebase
from AI_component.components.command_check import command_check
from AI_component.components.gemini import get_response
from AI_component.components.lesson_introduction import get_introduce_transcript
from AI_component.firebase.outline_handler import get_outline, generate_outline
from AI_component.time_measure import timeit
from AI_component import prompts
from AI_component.firebase.content_handler import get_content
from AI_component.components.search import get_search_result, get_urls
from AI_component.components.crawl_data import crawl_from_urls
from AI_component.utils import complete_prompt

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
def prompt_processing(prompt: Prompt, background_tasks: BackgroundTasks):
    if prompt is None:
        return {
            "error": "Prompt is None"
        }
    # Detect action/prompt
    detect_action = command_check(prompt.prompt_content)
    if detect_action != -1:
        return {
            "type": "action",
            "action_type": detect_action
        }

    logging.info("Handling the prompt...")
    if prompt.first_time:
        response = handle_first_time(prompt)
        background_tasks.add_task(generate_outline, prompt, prompt.user_info['secret_user_key'])
        background_tasks.add_task(get_content, prompt, get_outline(prompt.user_info['secret_user_key']))
        return {
            "type": "prompt",
            "outline": get_outline(prompt.user_info['secret_user_key']),
            "result": response,
            "images": []
        }
    
    # RAG-like process
    # Extract
    extract_info = get_response(extract_user_requirement(prompt.prompt_content, prompt.user_info['name']))
    # Search
    search_result = get_search_result(extract_info['query'])
    page_urls, image_urls = get_urls(search_result)
    # Crawl
    text_data = crawl_from_urls(page_urls)

    # Get response
    response = get_response(complete_prompt(text_data,prompt.prompt_content))

    # Return the result
    return {
        "type": "prompt",
        "outline": prompt.outline,
        "result": response,
        "images": image_urls
    }
    
@timeit
def handle_first_time(prompt):
    response = get_response(prompts.handle_first_time_prompt(str(prompt.prompt_content), str(prompt.user_info['name'])))
    # Do other first-time things
    return response
