from fastapi import APIRouter, status, Body
from app.utils import login as utils


router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK, summary="Login")
def login(username: str = Body(...), password: str = Body(...)):
    return utils.login(username, password)
