from fastapi import APIRouter, Body
from app.utils import user as utils


router = APIRouter()


@router.post("/", summary="User create")
def user_create(username: str = Body(...), password: str = Body(...), email: str = Body(...)):
    return utils.user_create(username, password, email)


@router.delete("/", summary="User delete")
def user_delete(user_id: int):
    return utils.user_delete(user_id)
