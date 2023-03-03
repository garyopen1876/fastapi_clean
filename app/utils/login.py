import bcrypt
from app.crud.crud_user import CRUDUser
from app.schemas.login import LoginRes
from app.setting import settings
from app.utils.app_error import UsernamePasswordError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from jose import jwt


def login(form_data: OAuth2PasswordRequestForm = Depends()) -> LoginRes:
    db = CRUDUser()
    db_password = db.get_user_password(form_data.username)
    if db_password and bcrypt.checkpw(
        form_data.password.encode("utf8"), db_password[0][0].encode("utf8")
    ):
        token = jwt.encode(
            {
                "username": form_data.username,
                "exp": datetime.utcnow()
                + timedelta(minutes=settings.token_limit_minutes),
            },
            settings.jwt_secret,
            algorithm="HS256",
        )
        return LoginRes(
            **{
                "message": "Login successfully",
                "token": token,
            }
        )
    raise UsernamePasswordError()
