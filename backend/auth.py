from jose import jwt
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET", "supersecret")

pwd = CryptContext(schemes=["bcrypt"])


def hash_password(password):
    return pwd.hash(password[:72])


def verify_password(password, hashed):
    return pwd.verify(password[:72], hashed)


def create_token(email):
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(days=7)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")