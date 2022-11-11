from app.utils.log import Logger
from app.utils.app_error import NoTokenError, TokenAuthenticateFailed
from fastapi import Request
from jose import jwt
import os

logger = Logger(level=__name__)


async def token_authentication(request: Request):
    token = request.headers.get("token")
    if not token:
        logger.error("No token provided.")
        raise NoTokenError()
    try:
        payload = jwt.decode(token, os.getenv(
            "JWT_SECRET"), algorithms=["HS256"])
        return payload
    except Exception as e:
        logger.error(f"""Failed to authenticate token, {e}""")
        raise TokenAuthenticateFailed(e)
