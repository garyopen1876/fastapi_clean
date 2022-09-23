from app.crud.base import CRUDBase
from app.db.db_models import User

import bcrypt


class CRUDUser(CRUDBase):

    def user_create(self, username: str, password: str, email: str):
        try:
            user = User(
                username=username,
                password=bcrypt.hashpw(
                    password.encode('utf8'), bcrypt.gensalt(12)),
                email=email
            )
            self.db.add(user)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def user_delete(self, user_id: int):
        try:
            user = self.db.query(User).filter(User.id == user_id).one()
            self.db.delete(user)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
