from fastapi import APIRouter
from app.schemas.item import Item

router = APIRouter()

fake_db = {}

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return fake_db.get(item_id, {"error": "Item not found"})

@router.post("/items/")
def create_item(item: Item):
    fake_db[item.id] = item.dict()
    return {"msg": "Item created", "item": item}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        return {"error": "Item not found"}
    fake_db[item_id] = item.dict()
    return {"msg": "Item updated", "item": item}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"msg": "Item deleted"}
    return {"error": "Item not found"}