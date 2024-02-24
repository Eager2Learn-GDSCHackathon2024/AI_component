import requests
import os

def get_search_result(query):
    url = 'https://customsearch.googleapis.com/customsearch/v1'
    params = {
        'cr': 'countryVN',
        'cx': os.getenv('cx'),
        'dateRestrict': 'y2',
        'exactTerms': 'phân số',
        'gl': 'vn',
        'lr': 'lang_vn',
        'num': '5',
        'q': query,
        'safe': 'active',
        'key': os.getenv('search_key')
    }
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data

def get_urls(data):
    """
    To get lists of url for crawling data
    output:
    tuple(page_list, images_list)
    """
    pass

