from app.crud.base import CRUDBase
from app.db.db_models import User

import bcrypt


class CRUDUser(CRUDBase):

    def user_create(self, username: str, password: str, email: str):
        try:
            user = User(
                username=username,
                password=bcrypt.hashpw(
                    password.encode('utf8'), bcrypt.gensalt(12)
                    ).decode(),
                email=email
            )
            self.db.add(user)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def user_delete(self, user_id: int):
        try:
            user = self.db.query(User).filter(User.id == user_id).one()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_password(self, username: str):
        try:
            query = self.db.query(
                User.password
            ).filter(
                User.username == username
            )
            return query.all()
        except Exception as e:
            self.db.rollback()
            raise e
