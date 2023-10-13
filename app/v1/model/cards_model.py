from sqlalchemy import (
    Column,
    Integer,
    String,
    LargeBinary
)
from app.v1.utils.db import Base


class Cards(Base):
    """cards"""

    __tablename__ = "cards"
    id_card = Column(Integer, primary_key=True, autoincrement=True)
    name_card = Column(String, nullable=False)
    type_card = Column(String, nullable=False)
    attack_value = Column(Integer, nullable=True)
    defence_value = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    bin_image = Column(LargeBinary, nullable=True)
