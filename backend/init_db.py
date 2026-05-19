from db import get_conn 

def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cv_profiles (
        id SERIAL PRIMARY KEY,
        cv_text TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_matches (
        id SERIAL PRIMARY KEY,
        cv_id INTEGER,
        job_title TEXT,
        score INTEGER,
        strengths TEXT,
        missing_skills TEXT
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()