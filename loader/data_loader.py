import psycopg2
from psycopg2.extras import execute_values
import logging


class DataLoader:
    def __init__(self, db_config):
        self.db_config = db_config

    def create_table(self):
        drop_table_query = "DROP TABLE IF EXISTS vacancies;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            company VARCHAR(255),
            salary_from VARCHAR(255),
            salary_to VARCHAR(255),
            salary_currency VARCHAR(50),
            location VARCHAR(255),
            published_at TIMESTAMP,
            description TEXT,
            url TEXT
        );
        """
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()
        try:
            cur.execute(drop_table_query)
            cur.execute(create_table_query)
            conn.commit()
            logging.info("Table 'vacancies' created successfully.")
        except Exception as e:
            conn.rollback()
            logging.error(f"Error creating table: {e}")
            raise e
        finally:
            cur.close()
            conn.close()

    def load_data(self, data):
        self.create_table()

        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()

        query = """
        INSERT INTO vacancies (title, company, salary_from, salary_to, salary_currency, location, published_at, description, url) VALUES %s
        """
        values = []
        for item in data['items']:
            title = item.get('name', '')
            company = item.get('employer', {}).get('name', '')
            salary_from = item.get('salary', {}).get('from', 'Not specified') if item.get('salary') else 'Not specified'
            salary_to = item.get('salary', {}).get('to', 'Not specified') if item.get('salary') else 'Not specified'
            salary_currency = item.get('salary', {}).get('currency', 'Not specified') if item.get(
                'salary') else 'Not specified'
            location = item.get('area', {}).get('name', '')
            published_at = item.get('published_at', '')
            description = item.get('snippet', {}).get('responsibility', '')
            url = item.get('alternate_url', '')
            values.append(
                (title, company, salary_from, salary_to, salary_currency, location, published_at, description, url))

        try:
            execute_values(cur, query, values)
            conn.commit()
            logging.info(f"{len(values)} records inserted successfully into 'vacancies' table.")
        except Exception as e:
            conn.rollback()
            logging.error(f"Error inserting data: {e}")
            raise e
        finally:
            cur.close()
            conn.close()
