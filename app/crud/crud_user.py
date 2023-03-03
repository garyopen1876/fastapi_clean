from app.crud.base import CRUDBase
from app.db.db_models import User

import bcrypt


class CRUDUser(CRUDBase):
    def create_user(self, username: str, password: str, email: str):
        try:
            user = User(
                username=username,
                password=bcrypt.hashpw(
                    password.encode("utf8"), bcrypt.gensalt(12)
                ).decode(),
                email=email,
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_user(self, username: str):
        try:
            user = self.db.query(User).filter(User.username == username).one()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_password(self, username: str):
        try:
            query = self.db.query(User.password).filter(User.username == username)
            return query.all()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_id_by_username(self, username: str):
        try:
            query = (
                self.db.query(User.id).filter(User.username == username).one_or_none()
            )
            if query:
                return query.id
            return query
        except Exception as e:
            self.db.rollback()
            raise e

    def update_user_password(self, user_id: int, password: str, commit: bool = True):
        try:
            self.db.query(User).filter(User.id == user_id).update(
                {
                    "password": bcrypt.hashpw(
                        password.encode("utf8"), bcrypt.gensalt(12)
                    ).decode()
                }
            )
            if commit:
                self.db.commit()
            else:
                self.db.flush()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
