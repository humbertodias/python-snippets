from pydantic import BaseModel
from typing import Optional

class PlayerCreate(BaseModel):
    name: str

class GameCreate(BaseModel):
    name: str
    genre: Optional[str] = None

class SessionCreate(BaseModel):
    game_id: int
    title: str

class JoinSession(BaseModel):
    player_id: int

class ScoreUpdate(BaseModel):
    player_id: int
    score: int

class PlayerResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class GameResponse(BaseModel):
    id: int
    name: str
    genre: Optional[str]

    class Config:
        orm_mode = True

class SessionResponse(BaseModel):
    id: int
    game_id: int
    title: str
    status: str

    class Config:
        orm_mode = True

class LeaderboardEntry(BaseModel):
    player_id: int
    score: int

    class Config:
        orm_mode = True
