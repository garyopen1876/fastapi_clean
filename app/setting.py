from pydantic import BaseSettings


class Settings(BaseSettings):
    # Develop Mode
    develop: bool
    # DB
    db_url: str = ""
    # JWT Token
    jwt_secret: str
    token_limit_minutes: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
