from app.utils import login as utils
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK, summary="Login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return utils.login(form_data)
