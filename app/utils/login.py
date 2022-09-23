from fastapi import HTTPException, status
from app.crud.crud_users import CRUDUser
from app.db.db_models import User

import bcrypt


def login(username: str, password: str):
    db = CRUDUser()
    user_password = db.get_user_password(username)
    
    if bcrypt.checkpw(password.encode('utf8'), user_password[0][0].encode('utf8')):
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail=f"login successfully"
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"username or password error"
    )
