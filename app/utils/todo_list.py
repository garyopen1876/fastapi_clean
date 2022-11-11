from app.crud.crud_todo_list import CRUDTodoList
from app.db.db_models import User, TodoList
from app.utils.app_error import UserNotExistedError, OperationFailed, TodoListNotExisted, NotTodoListOwner
from app.schemas.todo_list import TodoListData, TodoListCreate, TodoListDelete
from typing import Optional


def todo_list_read(page: Optional[int] = None):
    db = CRUDTodoList()
    list_data = db.get_todo_list_by_page(page)
    return TodoListData(**{"list_data": list_data})


def todo_list_create(username: str, message: str):
    db = CRUDTodoList()
    user = db.get_by_id_one_or_none(User, User.username, username)
    if not user:
        raise UserNotExistedError()
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


def todo_list_delete(username: str, todo_list_id: int):
    db = CRUDTodoList()
    user = db.get_by_id_one_or_none(User, User.username, username)
    if not user:
        raise UserNotExistedError()

    todo_list = db.get_by_id_one_or_none(TodoList, TodoList.id, todo_list_id)
    if not todo_list:
        raise TodoListNotExisted()

    if todo_list.user != user.id:
        raise NotTodoListOwner()

    try:
        db.delete_todo_list_by_id(todo_list_id)
        return TodoListDelete(**{"message": "Todo List delete successfully"})
    except Exception as e:
        raise OperationFailed(e)
