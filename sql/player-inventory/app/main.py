from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import SessionLocal
from models import Player
from schemas import PlayerCreate

from service import gain_xp

from models import Inventory
from service import add_item, get_inventory, use_item

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/players")
def create_player(data: PlayerCreate, db: Session = Depends(get_db)):
    player = Player(name=data.name)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


@app.post("/players/{player_id}/xp")
def add_xp(player_id: int, amount: int, db: Session = Depends(get_db)):
    return gain_xp(db, player_id, amount)


@app.get("/players")
def list_players(db: Session = Depends(get_db)):
    return db.query(Player).all()


@app.post("/players/{player_id}/items")
def give_item(player_id: int, item_id: int, quantity: int = 1, db: Session = Depends(get_db)):
    return add_item(db, player_id, item_id, quantity)

@app.get("/players/{player_id}/inventory")
def inventory(player_id: int, db: Session = Depends(get_db)):
    return get_inventory(db, player_id)

@app.post("/players/{player_id}/use-item")
def use(player_id: int, item_id: int, db: Session = Depends(get_db)):
    return use_item(db, player_id, item_id)

@app.get("/players/{player_id}/items")
def get_all_items(player_id: int, db: Session = Depends(get_db)):
    return db.query(Inventory).filter(Inventory.player_id == player_id).all()