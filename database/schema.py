def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            vacancy_id VARCHAR(50),
            name VARCHAR(255),
            area_name VARCHAR(255),
            salary_from INTEGER,
            salary_to INTEGER,
            salary_currency VARCHAR(10),
            employer_name VARCHAR(255),
            requirement TEXT,
            responsibility TEXT,
            experience VARCHAR(50),
            employment VARCHAR(50),
            schedule VARCHAR(50),
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            url TEXT
        );
        """)
        conn.commit()
