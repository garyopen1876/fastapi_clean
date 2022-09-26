from email.message import Message
from fastapi import HTTPException, status
from app.crud.crud_users import CRUDUser
from jose import jwt
from dotenv import load_dotenv
import datetime
import bcrypt
import os

load_dotenv()


def login(username: str, password: str):
    db = CRUDUser()

    user_password = db.get_user_password(username)

    if user_password and bcrypt.checkpw(password.encode('utf8'), user_password[0][0].encode('utf8')):
        token = jwt.encode({"username": username, "exp": datetime.datetime.now() + datetime.timedelta(seconds=5)},
                           os.getenv("JWT_SECRET"), algorithm="HS256")
        return {"message": "Login successfully", "token": token}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Username or Password error"
    )
