from pydantic import BaseModel


class TodoListData(BaseModel):
    list_data: list


class TodoListCreate(BaseModel):
    message: str
