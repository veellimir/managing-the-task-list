from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from settings.database import Base
from mixins.id_int_pk import IdIntPkMixin


class User(IdIntPkMixin, Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True)
    password_hash = Column(String)


class Task(IdIntPkMixin, Base):
    __tablename__ = "tasks"

    title = Column(String)
    description = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

