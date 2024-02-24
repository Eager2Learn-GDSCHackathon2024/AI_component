"""
Script to check if it's command or not
"""
import logging

import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from sentence_transformers import SentenceTransformer

from AI_component.utils import cosine_similarity

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

COMMANDS = [
    "cho tôi chuyển hoặc sang bài học tiếp theo hoặc bài học sau",
    "cho tôi chuyển hoặc quay lại bài học trước đó",
    "cho tôi xóa toàn bộ bảng"
]
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')


def command_check(input_prompt, threshold=0.75):
    input_prompt = input_prompt.lower()
    result = np.zeros(3)
    # BLEU score
    # reference = [
    #     sent.split() for sent in COMMANDS
    # ]
    # candidate = 'Hãy cho tôi sang bài học tiếp theo'.split()
    # for ref in reference:
    #     # print(sentence_bleu([ref], candidate, weights=(0.75, 0.25, 0.0, 0.0)))
    #     result = np.append(result, sentence_bleu([ref], candidate, weights=(0.75, 0.25, 0.0, 0.0)))
    # print(result)
    # Sentence similarity
    
    ref_embeddings = model.encode(COMMANDS)
    can_embedding = model.encode(input_prompt)
    result = (result + np.array([ cosine_similarity(em, can_embedding) for em in ref_embeddings]))
    print(np.array([ cosine_similarity(em, can_embedding) for em in ref_embeddings]))
    if result[np.argmax(result)] > threshold:
        return int(np.argmax(result))
    return -1