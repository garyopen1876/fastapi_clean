from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.attributes import InstrumentedAttribute

from typing import Union, List

from app.db.db_connect import SessionLocal


class CRUDBase:
    def __init__(self):
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()

    def get_all(self, table: DeclarativeMeta):
        try:
            return self.db.query(table).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_by_id(
        self,
        table: DeclarativeMeta,
        table_id: InstrumentedAttribute,
        select_id: Union[int, str],
    ):
        try:
            return self.db.query(table).filter(table_id == select_id).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_by_id_one_or_none(
        self,
        table: DeclarativeMeta,
        table_id: InstrumentedAttribute,
        select_id: Union[int, str],
    ):
        try:
            return self.db.query(table).filter(table_id == select_id).one_or_none()
        except Exception as e:
            self.db.rollback()
            raise e

    def insert_new(self, insert_data_list: List[DeclarativeMeta]):
        try:
            for new_data in insert_data_list:
                try:
                    self.db.add(new_data)
                    self.db.commit()
                except IntegrityError:
                    self.db.rollback()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
