from app.crud.crud_todo_list import CRUDTodoList
from app.db.db_models import User, TodoList
from app.utils.app_error import UserNotExistedError, OperationFailed
from app.schemas.todo_list import TodoListData, TodoListCreate
from typing import Optional


def todo_list_read(page: Optional[int] = None):
    db = CRUDTodoList()
    list_data = db.get_todo_list_by_page(page)
    return TodoListData(**{"list_data": list_data})


def todo_list_create(username: str, message: str):
    db = CRUDTodoList()
    user = db.get_by_id_one_or_none(User, User.username, username)
    if user:
        try:
            db.insert_new(
                insert_data_list=[
                    TodoList(
                        user=user.id,
                        message=message,
                    )
                ]
            )
            return TodoListCreate(**{"message": "Todo List create successfully"})
        except Exception as e:
            raise OperationFailed(e)
    raise UserNotExistedError()
