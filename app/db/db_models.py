from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .db_connect import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class TodoList(Base):
    __tablename__ = "todolists"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String)
    time_created = Column(DateTime, default=datetime.now, nullable=False)
    time_updated = Column(DateTime, default=datetime.now, nullable=False)
