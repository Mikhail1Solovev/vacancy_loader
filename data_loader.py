import requests
import psycopg2
import json

db_params = {
    'dbname': 'mikhaildb',
    'user': 'mikhail',
    'password': '2275450q',
    'host': 'localhost',
    'port': '5433'
}

# URL для получения данных
url = "https://api.hh.ru/vacancies"

# Параметры для API-запроса
params = {
    'text': 'Python developer',
    'area': '1',  # Москва
    'per_page': '10'
}


def parse_salary(salary):
    if salary:
        return salary.get('from'), salary.get('to'), salary.get('currency')
    return None, None, None


try:
    # Получение данных из API
    response = requests.get(url, params=params)
    response.raise_for_status()  # Проверка на успешное выполнение запроса
    data = response.json()

    # Подключение к базе данных
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Вставка данных в таблицу
    insert_query = '''
    INSERT INTO vacancies (vacancy_id, name, area_name, employer_name, published_at, salary_from, salary_to, salary_currency, json_data)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    for item in data['items']:
        vacancy_id = item['id']
        name = item['name']
        area_name = item['area']['name']
        employer_name = item['employer']['name']
        published_at = item['published_at']
        salary_from, salary_to, salary_currency = parse_salary(item.get('salary'))
        json_data = json.dumps(item)

        cursor.execute(insert_query, (
        vacancy_id, name, area_name, employer_name, published_at, salary_from, salary_to, salary_currency, json_data))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded successfully")
except Exception as e:
    print(f"An error occurred: {e}")
