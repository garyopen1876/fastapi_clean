import bcrypt
from app.crud.crud_users import CRUDUser
from app.db.db_models import User
from app.schemas.users import (
    CreateUserData,
    CreateUserRes,
    DeleteUserRes,
    ResetUserPasswordData,
    ResetUserPasswordRes,
)
from app.utils.app_error import (
    UsernameExistedError,
    EmailExistedError,
    UserNotExistedError,
    PasswordError,
)
from app.utils.verify import token_authentication


def create_user(data: CreateUserData) -> CreateUserRes:
    db = CRUDUser()
    if db.get_by_id_one_or_none(User, User.username, data.username):
        raise UsernameExistedError()
    if db.get_by_id_one_or_none(User, User.email, data.email):
        raise EmailExistedError()

    db.user_create(data.username, data.password, data.email)
    return CreateUserRes(**{"message": "User create successfully"})


def delete_user(token: str) -> DeleteUserRes:
    token_analyze = token_authentication(token)
    db = CRUDUser()
    if not db.get_by_id_one_or_none(User, User.username, token_analyze["username"]):
        raise UserNotExistedError()

    db.user_delete(token_analyze["username"])
    return DeleteUserRes(**{"message": "User delete successfully"})


def reset_user_password(
    data: ResetUserPasswordData, token: str
) -> ResetUserPasswordRes:
    token_analyze = token_authentication(token)
    db = CRUDUser()
    user = db.get_by_id_one_or_none(User, User.username, token_analyze["username"])
    if not user:
        raise UserNotExistedError()

    if bcrypt.checkpw(data.old_password.encode("utf8"), user.password.encode("utf8")):
        db.update_user_password(user.id, data.new_password)
        return ResetUserPasswordRes(**{"message": "User password reset successfully"})

    raise PasswordError()
