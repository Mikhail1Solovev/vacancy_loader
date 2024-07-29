import psycopg2
from config import DB_CONFIG

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(**DB_CONFIG)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

def get_db_connection():
    return DatabaseConnection()
