from app.crud.crud_message import CRUDMessage
from app.crud.crud_user import CRUDUser
from app.schemas.message import CreateMessageData
from app.utils.app_error import UserNotExistedError
from app.utils.verify import token_authentication


def get_message(page: int, keyword: str):
    db = CRUDMessage()
    message = db.get_message(page, keyword)
    return message


def create_message(data: CreateMessageData, token: str):
    token_analyze = token_authentication(token)
    user_id = CRUDUser().get_user_id_by_username(token_analyze["username"])
    if not user_id:
        raise UserNotExistedError()
    CRUDMessage().create_message(data.title, data.content, user_id)
    return {"message": "Create Message Successfully"}
