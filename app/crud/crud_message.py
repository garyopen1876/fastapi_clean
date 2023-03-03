from app.crud.base import CRUDBase
from app.db.db_models import Message
from app.setting import settings
from datetime import datetime


class CRUDMessage(CRUDBase):
    def get_message(self, page: int, keyword: str):
        query = self.db.query(Message)
        if keyword:
            query.filter(
                Message.title.like("%{}%".format(keyword)),
                Message.content.like("%{}%".format(keyword)),
            )
        if page:
            query.limit(settings.page_size).offset((page - 1) * settings.page_size)
        return query.all()

    def create_message(self, title: str, content: str, user_id: int):
        try:
            message = Message(
                user_id=user_id,
                title=title,
                content=content,
                create_time=datetime.utcnow(),
                update_time=datetime.utcnow(),
            )
            self.db.add(message)
            self.db.commit()
            self.db.refresh(message)
            return True
        except Exception as e:
            self.db.rollback()
            raise e
