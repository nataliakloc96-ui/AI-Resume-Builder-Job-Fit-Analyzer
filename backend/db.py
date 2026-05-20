import psycopg2
import os
from config import DATABSASE_URL

def get_conn():
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise Exception("DATABASE_URL is missing in environment variables")


    return psycopg2.connect(db_url)