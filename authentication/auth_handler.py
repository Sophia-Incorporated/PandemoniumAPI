import time
from typing import Dict
from models.user import User

import jwt
from config import Settings


JWT_SECRET = Settings.jwt_secret
JWT_ALGORITHM = Settings.jwt_algorithm

def return_token(token: str):
    return {
        "access_token" : token
    }

def encode(User: User) -> Dict[str, str]:
    payload = {
        "id": User.id,
        "email": User.email,
        "first_name": User.first_name,
        "last_name": User.last_name,
        "is_admin": User.is_admin,
        "expires": time.time() + 600,
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return_token(token)

def decode(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}