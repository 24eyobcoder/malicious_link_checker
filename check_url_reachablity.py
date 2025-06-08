import requests
from urllib.parse import urlparse

def check_url_reachablity(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except Exception as e:
        return False
            
   