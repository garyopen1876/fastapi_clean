from fastapi import APIRouter, status, Body, Depends
from app.utils import user as utils
from app.middleware.token_authentication import token_authentication

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, summary="User create", dependencies=[Depends(token_authentication)])
def user_create(username: str = Body(...), password: str = Body(...), email: str = Body(...)):
    return utils.user_create(username, password, email)


@router.delete("/", status_code=status.HTTP_200_OK, summary="User delete", dependencies=[Depends(token_authentication)])
def user_delete(user_id: int):
    return utils.user_delete(user_id)


@router.put("/reset_password", status_code=status.HTTP_200_OK, summary="User reset password", dependencies=[Depends(token_authentication)])
def user_reset_password(username: str = Body(...), old_password: str = Body(...), new_password: str = Body(...)):
    return utils.user_reset_password(username,  old_password,  new_password)
