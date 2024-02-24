import json
import logging

from AI_component.firebase import ref
from AI_component.components.gemini import get_response
from AI_component import prompts
from AI_component.time_measure import timeit

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_outline(secret_user_key):
    if secret_user_key not in ref.get().keys():
        return {
            "error" : "first time so no outline yet"
        }
    return ref.get()[secret_user_key]['outline']

@timeit
def generate_outline(prompt, secret_user_key, RAG : bool = False):
    # Without RAG first
    response = None
    while not isinstance(response, dict):
        response = get_response(prompts.generate_outline_prompt(prompt.prompt_content))
        logging.info(f"Response outline gen: {response}")
        try:
            response = json.loads(response)
        except:
            continue
    # Insert into firebase
    ref.set({
        secret_user_key: {
            "outline": response
        }
    })
