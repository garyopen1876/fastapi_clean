from pydantic import BaseModel


class CreateMessageData(BaseModel):
    title: str
    content: str
