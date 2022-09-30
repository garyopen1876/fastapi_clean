from pydantic import BaseModel


class UserCreate(BaseModel):
    message: str


class UserDelete(BaseModel):
    message: str


class UserResetPassword(BaseModel):
    message: str
