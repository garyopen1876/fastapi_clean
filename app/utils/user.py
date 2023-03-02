import bcrypt
from app.crud.crud_users import CRUDUser
from app.db.db_models import User
from app.schemas.users import UserCreate, UserDelete, UserResetPassword
from app.utils.app_error import (
    UsernameExistedError,
    EmailExistedError,
    UserNotExistedError,
    PasswordError,
)
from app.utils.verify import token_authentication


def user_create(username: str, password: str, email: str) -> UserCreate:
    db = CRUDUser()
    if db.get_by_id_one_or_none(User, User.username, username):
        raise UsernameExistedError()
    if db.get_by_id_one_or_none(User, User.email, email):
        raise EmailExistedError()

    db.user_create(username, password, email)
    return UserCreate(**{"message": "User create successfully"})


def user_delete(token: str) -> UserDelete:
    token_analyze = token_authentication(token)
    db = CRUDUser()
    if not db.get_by_id_one_or_none(User, User.username, token_analyze["username"]):
        raise UserNotExistedError()

    db.user_delete(token_analyze["username"])
    return UserDelete(**{"message": "User delete successfully"})


def user_reset_password(
    token: str, old_password: str, new_password: str
) -> UserResetPassword:
    token_analyze = token_authentication(token)
    db = CRUDUser()
    user = db.get_by_id_one_or_none(User, User.username, token_analyze["username"])
    if not user:
        raise UserNotExistedError()

    if bcrypt.checkpw(old_password.encode("utf8"), user.password.encode("utf8")):
        db.update_user_password(user.id, new_password)
        return UserResetPassword(**{"message": "User password reset successfully"})

    raise PasswordError()
