from fastapi import HTTPException, status
from app.crud.crud_users import CRUDUser
from app.db.db_models import User


def user_create(username: str, password: str, email: str):
    db = CRUDUser()
    if db.get_by_id_one_or_none(User, User.username, username):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"username existed"
        )
    if db.get_by_id_one_or_none(User, User.email, email):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"email existed"
        )

    try:
        db.user_create(username, password, email)
        return {"Message": "user create successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )


def user_delete(user_id: int):
    db = CRUDUser()
    if not db.get_by_id_one_or_none(User, User.id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"user not existed"
        )
    try:
        db.user_delete(user_id)
        return {"Message": "user delete successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )
