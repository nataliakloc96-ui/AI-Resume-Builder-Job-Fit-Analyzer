import os
import psycopg2

DATABSASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
FRONTEND_URL = os.getenv("FRONTEND_URL")

def get_conn():
    return.psycopg2.connect(DATABASE_URL, sslmode="require")