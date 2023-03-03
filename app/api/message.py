from app.utils import message as utils
from fastapi import APIRouter, status, Depends, Body

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get Message",
)
def get_message(page: int = None, key_word: str = None):
    return utils.get_message(page, key_word)
