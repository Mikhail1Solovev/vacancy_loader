from loader.logger import Logger
from loader.vacancy_loader import VacancyLoader
from config import API_URL
import time

if __name__ == '__main__':
    Logger.setup_logging()
    json_file = 'data.json'
    vacancy_loader = VacancyLoader(API_URL, json_file)
    vacancy_loader.run()

    # Бесконечный цикл, чтобы контейнер оставался активным
    while True:
        time.sleep(10)
