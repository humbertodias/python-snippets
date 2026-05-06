from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP)

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    genre = Column(String)
    created_at = Column(TIMESTAMP)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    started_at = Column(TIMESTAMP)
    status = Column(String, default="active")

class SessionPlayer(Base):
    __tablename__ = "session_players"

    session_id = Column(Integer, ForeignKey("sessions.id", ondelete="CASCADE"), primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), primary_key=True)
    score = Column(Integer, default=0)
