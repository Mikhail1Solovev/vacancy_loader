from database.connection import get_db_connection
from database.schema import create_tables

def setup_database():
    with get_db_connection() as conn:
        create_tables(conn)
