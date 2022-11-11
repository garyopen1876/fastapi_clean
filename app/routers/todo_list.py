from app.utils import todo_list as utils
from app.middleware.token_authentication import token_authentication
from fastapi import APIRouter, status, Body, Depends
from typing import Optional

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, summary="Todo List read", dependencies=[Depends(token_authentication)])
def todo_list_read(page: Optional[int] = None):
    return utils.todo_list_read(page)


@router.post("/", status_code=status.HTTP_200_OK, summary="Todo List create")
def todo_list_create(token_payload: dict = Depends(token_authentication), message: str = Body(..., embed=True)):
    return utils.todo_list_create(token_payload["username"], message)


@router.delete("/{todo_list_id}", status_code=status.HTTP_200_OK, summary="Todo List delete")
def todo_list_delete(todo_list_id: int, token_payload: dict = Depends(token_authentication)):
    return utils.todo_list_delete(token_payload["username"], todo_list_id)

