import json
import logging

from AI_component.firebase import ref
from AI_component.components.gemini import get_response
from AI_component import prompts
from AI_component.time_measure import timeit

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_content(prompt, outline):
    """
    Get content given prompt and outline
    """
    pass