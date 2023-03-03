from fastapi import APIRouter, status, Body, Depends
from app.schemas.users import CreateUser 
from app.setting import oauth2_token
from app.utils import user as utils


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="User create",
)
def user_create(
    username: str,
    password: str,
    email: str,
):
    return utils.user_create(username, password, email)


@router.delete(
    "",
    status_code=status.HTTP_200_OK,
    summary="User delete",
)
def user_delete(token=Depends(oauth2_token)):
    return utils.user_delete(token)


@router.put(
    "/reset/password",
    status_code=status.HTTP_200_OK,
    summary="User reset password",
)
def user_reset_password(
    old_password: str = Body(...),
    new_password: str = Body(...),
    token: str = Depends(oauth2_token),
):
    return utils.user_reset_password(token, old_password, new_password)
