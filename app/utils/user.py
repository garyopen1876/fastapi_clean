from fastapi import HTTPException, status
from app.crud.crud_users import CRUDUser
from app.db.db_models import User


def user_create(username: str, password: str, email: str):
    db = CRUDUser()
    if db.get_by_id_one_or_none(User, User.username, username):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Username existed"
        )
    if db.get_by_id_one_or_none(User, User.email, email):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Email existed"
        )

    db.user_create(username, password, email)
    raise HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail=f"User create successfully"
    )


def user_delete(user_id: int):
    db = CRUDUser()
    if not db.get_by_id_one_or_none(User, User.id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User not existed"
        )
        
    db.user_delete(user_id)
    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=f"User delete successfully"
    )
