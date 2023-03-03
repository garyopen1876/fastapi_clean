from fastapi import APIRouter, status, Depends
from app.schemas.users import CreateUserData, ResetUserPasswordData
from app.setting import oauth2_token
from app.utils import user as utils


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create User",
)
def create_user(data: CreateUserData):
    return utils.create_user(data)


@router.delete(
    "",
    status_code=status.HTTP_200_OK,
    summary="Delete User",
)
def delete_user(token=Depends(oauth2_token)):
    return utils.delete_user(token)


@router.put(
    "/reset/password",
    status_code=status.HTTP_200_OK,
    summary="Reset User Password",
)
def reset_user_password(
    data: ResetUserPasswordData,
    token: str = Depends(oauth2_token),
):
    return utils.reset_user_password(data, token)
