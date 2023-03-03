from app.utils import message as utils
from app.schemas.message import CreateMessageData
from app.setting import oauth2_token
from fastapi import APIRouter, status, Depends

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get Message",
)
def get_message(page: int = None, keyword: str = None):
    return utils.get_message(page, keyword)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create Message",
)
def create_message(data: CreateMessageData, token=Depends(oauth2_token)):
    return utils.create_message(data, token)
