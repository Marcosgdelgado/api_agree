from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.v1.utils.db import Base


class CardsDeck(Base):
    """Cards Deck"""

    __tablename__ = "cards_deck"
    id_deck = Column(Integer, primary_key=True, autoincrement=True)
    id_owner = Column(Integer, ForeignKey("users.user_id"))
    deck_name = Column(String, nullable=False)
    cards_list = Column(String, nullable=False)
