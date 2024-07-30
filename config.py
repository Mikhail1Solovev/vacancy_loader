import os

DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'mikhaildb'),
    'user': os.getenv('DB_USER', 'mikhail'),
    'password': os.getenv('DB_PASSWORD', '2275450q'),
    'host': os.getenv('DB_HOST', 'db'),
    'port': os.getenv('DB_PORT', '5432')
}

API_URL = "https://api.hh.ru/vacancies?text=Python+developer"
