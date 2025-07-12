from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.item import Item, ItemStatus
from app.models.user import User
from app.schemas.item import ItemCreate, ItemResponse
from app.dependencies import get_current_user

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#1. Get all approved items
@router.get("/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.status == ItemStatus.approved).all()


#2. Get item by ID
@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


#3. Add a new item
@router.post("/", response_model=ItemResponse)
def add_item(item: ItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_item = Item(**item.dict(), owner_id=current_user.id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
