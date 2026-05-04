from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    gold = Column(Integer, default=0)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Inventory(Base):
    __tablename__ = "inventory"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    quantity = Column(Integer, default=1)