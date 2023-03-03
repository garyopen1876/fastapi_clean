from pydantic import BaseModel


class CreateUserData(BaseModel):
    username: str
    password: str
    email: str


class ResetUserPasswordData(BaseModel):
    old_password: str
    new_password: str


class CreateUserRes(BaseModel):
    message: str


class DeleteUserRes(BaseModel):
    message: str


class ResetUserPasswordRes(BaseModel):
    message: str
