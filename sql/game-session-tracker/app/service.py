from models import Player, Game, Session, SessionPlayer


def create_player(db, name):
    player = Player(name=name)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def create_game(db, name, genre=None):
    game = Game(name=name, genre=genre)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game


def create_session(db, game_id, title):
    session = Session(game_id=game_id, title=title)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def join_session(db, session_id, player_id):
    membership = db.query(SessionPlayer).filter_by(
        session_id=session_id,
        player_id=player_id
    ).first()
    if membership:
        return membership

    membership = SessionPlayer(session_id=session_id, player_id=player_id, score=0)
    db.add(membership)
    db.commit()
    return membership


def update_score(db, session_id, player_id, score):
    membership = db.query(SessionPlayer).filter_by(
        session_id=session_id,
        player_id=player_id
    ).first()
    if not membership:
        return {"error": "player not joined"}

    membership.score = score
    db.commit()
    return membership


def get_sessions(db):
    return db.query(Session).all()


def get_session(db, session_id):
    return db.query(Session).filter_by(id=session_id).first()


def get_leaderboard(db, session_id):
    return db.query(SessionPlayer).filter_by(session_id=session_id).order_by(SessionPlayer.score.desc()).all()


def list_players(db):
    return db.query(Player).all()


def list_games(db):
    return db.query(Game).all()
