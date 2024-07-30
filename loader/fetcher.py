import requests
import json
import logging

class DataFetcher:
    def __init__(self, api_url, json_file):
        self.api_url = api_url
        self.json_file = json_file

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            with open(self.json_file, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info('Data fetched and saved to JSON file.')
        else:
            logging.error(f'Failed to fetch data. Status code: {response.status_code}')
            response.raise_for_status()
