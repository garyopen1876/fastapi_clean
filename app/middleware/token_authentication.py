from fastapi import Request
from fastapi import HTTPException, Request
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()


async def token_authentication(request: Request):
    token = request.headers.get("token")
    if not token:
        raise HTTPException(status_code=403, detail="No token provided")
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(
            status_code=402, detail=f"Failed to authenticate token, {e}")
