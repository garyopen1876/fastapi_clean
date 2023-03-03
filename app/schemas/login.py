from pydantic import BaseModel


class LoginRes(BaseModel):
    message: str
    token: str
