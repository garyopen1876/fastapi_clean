from pydantic import BaseSettings
from fastapi.security import OAuth2PasswordBearer

oauth2_token = OAuth2PasswordBearer(tokenUrl="/login")


class Settings(BaseSettings):
    # Develop Mode
    develop: bool
    # DB
    db_url: str = ""
    # JWT Token
    jwt_secret: str
    token_limit_minutes: int = 10
    # Log
    log_path: str = "./tmp/logs"
    # Page
    page_size: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
