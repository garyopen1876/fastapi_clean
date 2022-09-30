from app.crud.crud_users import CRUDUser
from app.setting import settings
from app.schemas.login import LoginMessage
from app.utils.app_error import UsernamePasswordError
from datetime import datetime, timedelta
from jose import jwt

import bcrypt


def login(username: str, password: str) -> LoginMessage:
    db = CRUDUser()

    user_password = db.get_user_password(username)
    if user_password and bcrypt.checkpw(password.encode('utf8'), user_password[0][0].encode('utf8')):
        token = jwt.encode({"username": username, "exp": datetime.utcnow() + timedelta(minutes=settings.token_limit_minutes)},
                           settings.jwt_secret, algorithm="HS256")
        return LoginMessage(**{"message": "Login successfully", "token": token})

    raise UsernamePasswordError()
