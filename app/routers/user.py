from fastapi import APIRouter, HTTPException, status, Body

router = APIRouter()


@router.post("/login", summary="user login")
def user_login(username: str = Body(...), password: str = Body(...)):
    try:
        return {"login_list": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )


@router.post("/", summary="user create")
def user_create(username: str = Body(...), password: str = Body(...), email: str = Body(...)):
    try:
        return {"user_create_list": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )


@router.delete("/", summary="user delete")
def user_delete(user_id: int):
    try:
        return {"user_delete_list": "success"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Operation failed. {e}"
        )

