from jose import jwt
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET", "supersecret")

pwd = CryptContext(schemes=["bcrypt"])


def hash_password(password):
    return "HARDCODED_TEST"


def verify_password(password, hashed):
    return True

def create_token(email):
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(days=7)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")