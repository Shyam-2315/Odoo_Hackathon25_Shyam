from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.item import Item, ItemStatus
from app.models.user import User
from app.database import SessionLocal
from app.dependencies import get_current_user
from app.schemas.item import ItemResponse

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#1. View Pending Items
@router.get("/pending-items", response_model=List[ItemResponse])
def view_pending_items(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can view pending items")
    return db.query(Item).filter(Item.status == ItemStatus.pending).all()


#2. Approve Item
@router.post("/approve/{item_id}")
def approve_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can approve items")

    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.status = ItemStatus.approved
    item.is_available = True
    db.commit()
    return {"message": "Item approved successfully"}


#3. Reject/Remove Item
@router.post("/reject/{item_id}")
def reject_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can reject items")

    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item rejected and removed"}
