from sqlalchemy import Column, Integer, String
from app.v1.utils.db import Base


class Users(Base):
    """Users"""

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    user_pass = Column(String, nullable=False)
