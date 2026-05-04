from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str

class PlayerResponse(BaseModel):
    id: int
    name: str
    level: int
    xp: int
    gold: int

class ItemResponse(BaseModel):
    id: int
    name: str


class InventoryResponse(BaseModel):
    item_id: int
    quantity: int