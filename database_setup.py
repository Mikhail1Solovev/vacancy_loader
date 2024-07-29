import psycopg2

db_params = {
    'dbname': 'mikhaildb',
    'user': 'mikhail',
    'password': '2275450q',
    'host': 'localhost',
    'port': '5433'  # Измените порт здесь на 5433
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS vacancies (
        id SERIAL PRIMARY KEY,
        vacancy_id VARCHAR(255),
        name VARCHAR(255),
        area_name VARCHAR(255),
        employer_name VARCHAR(255),
        published_at TIMESTAMP,
        salary_from NUMERIC,
        salary_to NUMERIC,
        salary_currency VARCHAR(10),
        json_data JSONB
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")
except Exception as e:
    print(f"An error occurred: {e}")
