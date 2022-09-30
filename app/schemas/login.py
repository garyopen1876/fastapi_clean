from pydantic import BaseModel


class LoginMessage(BaseModel):
    message: str
    token: str
