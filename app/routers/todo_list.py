from app.utils import todo_list as utils
from app.middleware.token_authentication import token_authentication
from fastapi import APIRouter, status, Body, Depends
from typing import Optional

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, summary="Todo List read")
def todo_list_read(page: Optional[int] = None):
    return utils.todo_list_read(page)


@router.post("/", status_code=status.HTTP_200_OK, summary="Todo List create")
def todo_list_create(username: str = Body(...), message: str = Body(...)):
    return utils.todo_list_create(username, message)
