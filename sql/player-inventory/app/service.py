from models import Player, Inventory, Item

def calculate_level(xp):
    return xp // 100 + 1


def gain_xp(db, player_id, amount):
    player = db.query(Player).get(player_id)

    player.xp += amount
    player.level = calculate_level(player.xp)

    db.commit()
    db.refresh(player)

    return player

def add_item(db, player_id, item_id, quantity=1):
    inv = db.query(Inventory).filter_by(
        player_id=player_id,
        item_id=item_id
    ).first()

    if inv:
        inv.quantity += quantity
    else:
        inv = Inventory(
            player_id=player_id,
            item_id=item_id,
            quantity=quantity
        )
        db.add(inv)

    db.commit()
    return inv


def get_inventory(db, player_id):
    return db.query(Inventory).filter_by(player_id=player_id).all()


def use_item(db, player_id, item_id):
    inv = db.query(Inventory).filter_by(
        player_id=player_id,
        item_id=item_id
    ).first()

    if not inv or inv.quantity <= 0:
        return {"error": "item not found"}

    inv.quantity -= 1

    # exemplo simples: potion dá XP
    if item_id == 3:  # Potion
        player = db.query(Player).get(player_id)
        player.xp += 50
        player.level = player.xp // 100 + 1

    if inv.quantity == 0:
        db.delete(inv)

    db.commit()
    return {"message": "item used"}