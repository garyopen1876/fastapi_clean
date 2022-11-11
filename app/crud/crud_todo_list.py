from app.crud.base import CRUDBase
from app.db.db_models import TodoList
from app.setting import settings
from typing import Optional


class CRUDTodoList(CRUDBase):
    def get_todo_list_by_page(self, page: Optional[int] = None):
        try:
            if page:
                max_data = settings.each_page_data*page
                list_data = self.db.query(TodoList).filter(
                )[max_data-settings.each_page_data:max_data]
            else:
                list_data = self.db.query(TodoList).all()
            return list_data
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_todo_list_by_id(self, todo_list_id: int):
        try:
            self.db.query(TodoList).filter_by(id=todo_list_id).delete()
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
