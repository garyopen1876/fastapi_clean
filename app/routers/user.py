from fastapi import APIRouter, status, Body, Depends
from app.setting import oauth2_token
from app.utils import user as utils


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="User create",
)
def user_create(
    username: str = Body(...),
    password: str = Body(...),
    email: str = Body(...),
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
    "/reset_password",
    status_code=status.HTTP_200_OK,
    summary="User reset password",
)
def user_reset_password(
    token: str = Depends(oauth2_token),
    old_password: str = Body(...),
    new_password: str = Body(...),
):
    return utils.user_reset_password(token, old_password, new_password)
