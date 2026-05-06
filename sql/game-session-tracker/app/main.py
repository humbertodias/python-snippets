from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import SessionLocal
from schemas import (
    PlayerCreate,
    GameCreate,
    SessionCreate,
    JoinSession,
    ScoreUpdate,
    PlayerResponse,
    GameResponse,
    SessionResponse,
    LeaderboardEntry,
)
from service import (
    create_player,
    create_game,
    create_session,
    join_session,
    update_score,
    get_sessions,
    get_session,
    get_leaderboard,
    list_players,
    list_games,
)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/players", response_model=PlayerResponse)
def post_player(data: PlayerCreate, db: Session = Depends(get_db)):
    return create_player(db, data.name)


@app.post("/games", response_model=GameResponse)
def post_game(data: GameCreate, db: Session = Depends(get_db)):
    return create_game(db, data.name, data.genre)


@app.post("/sessions", response_model=SessionResponse)
def post_session(data: SessionCreate, db: Session = Depends(get_db)):
    return create_session(db, data.game_id, data.title)


@app.post("/sessions/{session_id}/join")
def post_join(session_id: int, data: JoinSession, db: Session = Depends(get_db)):
    membership = join_session(db, session_id, data.player_id)
    if membership is None:
        raise HTTPException(status_code=404, detail="session or player not found")
    return membership


@app.post("/sessions/{session_id}/score")
def post_score(session_id: int, data: ScoreUpdate, db: Session = Depends(get_db)):
    result = update_score(db, session_id, data.player_id, data.score)
    if isinstance(result, dict) and result.get("error"):
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/players", response_model=list[PlayerResponse])
def list_players_endpoint(db: Session = Depends(get_db)):
    return list_players(db)


@app.get("/games", response_model=list[GameResponse])
def list_games_endpoint(db: Session = Depends(get_db)):
    return list_games(db)


@app.get("/sessions", response_model=list[SessionResponse])
def list_sessions(db: Session = Depends(get_db)):
    return get_sessions(db)


@app.get("/sessions/{session_id}", response_model=SessionResponse)
def get_session_by_id(session_id: int, db: Session = Depends(get_db)):
    session = get_session(db, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="session not found")
    return session


@app.get("/sessions/{session_id}/leaderboard", response_model=list[LeaderboardEntry])
def get_session_leaderboard(session_id: int, db: Session = Depends(get_db)):
    return get_leaderboard(db, session_id)
