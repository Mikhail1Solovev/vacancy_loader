import requests
from database.connection import get_db_connection
from config import API_URL

class DataLoader:
    def __init__(self):
        self.api_url = API_URL

    def fetch_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()

    def insert_data(self, data):
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                for item in data['items']:
                    cur.execute("""
                        INSERT INTO vacancies (
                            vacancy_id, name, area, salary_min, salary_max, currency,
                            employer_name, requirement, responsibility, experience,
                            employment, schedule, created_at, updated_at, url
                        ) VALUES (
                            %(id)s, %(name)s, %(area)s, %(salary_min)s, %(salary_max)s, %(currency)s,
                            %(employer_name)s, %(requirement)s, %(responsibility)s, %(experience)s,
                            %(employment)s, %(schedule)s, %(created_at)s, %(updated_at)s, %(url)s
                        )
                    """, {
                        'id': item['id'],
                        'name': item['name'],
                        'area': item['area']['name'],
                        'salary_min': item['salary']['from'] if item['salary'] else None,
                        'salary_max': item['salary']['to'] if item['salary'] else None,
                        'currency': item['salary']['currency'] if item['salary'] else None,
                        'employer_name': item['employer']['name'],
                        'requirement': item['snippet']['requirement'],
                        'responsibility': item['snippet']['responsibility'],
                        'experience': item['experience']['name'],
                        'employment': item['employment']['name'],
                        'schedule': item['schedule']['name'],
                        'created_at': item['created_at'],
                        'updated_at': item['published_at'],
                        'url': item['alternate_url']
                    })
                conn.commit()

    def load_data(self):
        data = self.fetch_data()
        self.insert_data(data)
