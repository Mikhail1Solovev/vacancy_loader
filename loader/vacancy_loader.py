from loader.fetcher import DataFetcher
from loader.data_loader import DataLoader
from config import DB_CONFIG
import json

class VacancyLoader:
    def __init__(self, api_url, json_file):
        self.api_url = api_url
        self.json_file = json_file
        self.data_loader = DataLoader(DB_CONFIG)
        self.data_fetcher = DataFetcher(api_url, json_file)

    def run(self):
        self.data_fetcher.fetch_data()
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        self.data_loader.load_data(data)
