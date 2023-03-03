from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence, DateTime
from sqlalchemy.orm import relationship
from .db_connect import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=False)
    # one to many
    message_owner = relationship("Message", back_populates="user_id")


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, Sequence("message_id_seq"), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    title = Column(String, index=True)
    content = Column(String, nullable=True)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
