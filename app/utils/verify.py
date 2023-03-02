from app.setting import settings
from app.utils.log import Logger
from app.utils.app_error import NoTokenError, TokenAuthenticateFailed
from jose import jwt
import os

logger = Logger(level=__name__)


def token_authentication(token: str):
    if not token:
        logger.error("No token provided.")
        raise NoTokenError()
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except Exception as e:
        logger.error(f"""Failed to authenticate token, {e}""")
        raise TokenAuthenticateFailed(e)
