from pydantic import BaseSettings


class Settings(BaseSettings):
    # Develop Mode
    develop: bool
    # DB
    db_url: str = ""
    # JWT Token
    jwt_secret: str
    token_limit_minutes: int = 10
    # Log
    log_path:str = "./tmp/logs"
    # telegram
    telegram_api_token:str
    telegram_chat_id:str

    class Config:
        env_file = ".env"


settings = Settings()
