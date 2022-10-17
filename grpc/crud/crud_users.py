from crud.base import CRUDBase
from db.db_models import User


class CRUDUser(CRUDBase):

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