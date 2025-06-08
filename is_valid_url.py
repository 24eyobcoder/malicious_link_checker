import requests
from urllib.parse import urlparse

def is_valid_url(url):
    parsed=urlparse(url)
    return parsed.scheme in ['http', 'https'] and bool(parsed.netloc)

