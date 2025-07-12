from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.swap import Swap, SwapType, SwapStatus
from app.models.item import Item, ItemStatus
from app.schemas.swap import SwapRequest, SwapResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#1. Initiate a Swap or Redemption
@router.post("/", response_model=SwapResponse)
def request_swap(swap: SwapRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(Item).filter(Item.id == swap.item_id).first()

    if not item or item.status != ItemStatus.approved or not item.is_available:
        raise HTTPException(status_code=400, detail="Item not available for swap/redeem")

    if item.owner_id == current_user.id:
        raise HTTPException(status_code=403, detail="You can't request your own item")

    # Check if user has enough points if redeeming
    if swap.type == SwapType.redeem and current_user.points < 10:
        raise HTTPException(status_code=400, detail="Not enough points to redeem")

    new_swap = Swap(
        item_id=item.id,
        requester_id=current_user.id,
        type=swap.type,
        status=SwapStatus.pending
    )

    # Update item availability
    item.is_available = False
    item.status = ItemStatus.pending

    if swap.type == SwapType.redeem:
        current_user.points -= 10  

    db.add(new_swap)
    db.commit()
    db.refresh(new_swap)
    return new_swap


#2. List Swaps for Current User
@router.get("/", response_model=List[SwapResponse])
def get_my_swaps(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Swap).filter(Swap.requester_id == current_user.id).all()
