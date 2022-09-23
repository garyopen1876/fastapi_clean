from fastapi import APIRouter, Body
from app.utils import login as utils


router = APIRouter()


@router.post("/login", summary="login")
def login(username: str = Body(...), password: str = Body(...)):
    return utils.login(username, password)
    
