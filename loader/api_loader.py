import requests
from config import API_URL

class APILoader:
    def fetch_data(self):
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
