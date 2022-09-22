from typing import Union
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post("/login", summary="user login")
def read_item(username: str, password: str):
    try:
        return {"login_list": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )
