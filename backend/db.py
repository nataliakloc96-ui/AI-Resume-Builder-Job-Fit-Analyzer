import psycopg2
import os
from config import DATABSASE_URL

def get_conn():
    return psycopg2.connect(
        os.environ["DATABASE_URL"]
    )