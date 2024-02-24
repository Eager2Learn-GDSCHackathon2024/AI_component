import requests
from bs4 import BeautifulSoup

def crawl_from_urls(url_list):
    text_data = ""
    for url in url_list:
        result = crawl_text_from_url(url)
        if result is not None:
            text_data += result
    return text_data

def crawl_text_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all text data
            text_data = soup.get_text()
            
            return text_data
        else:
            print("Failed to fetch page, status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None