from sqlalchemy.orm import Session
from app.models import swap as swap_model
from app.schemas import swap as swap_schema

def create_swap(db: Session, swap: swap_schema.SwapCreate, offered_by_id: int):
    db_swap = swap_model.Swap(**swap.dict(), offered_by_id=offered_by_id)
    db.add(db_swap)
    db.commit()
    db.refresh(db_swap)
    return db_swap

def get_swaps_for_user(db: Session, user_id: int):
    return db.query(swap_model.Swap).filter(
        (swap_model.Swap.offered_by_id == user_id) | (swap_model.Swap.offered_to_id == user_id)
    ).all()

def update_swap_status(db: Session, swap_id: int, new_status: swap_schema.SwapStatus):
    db_swap = db.query(swap_model.Swap).filter(swap_model.Swap.id == swap_id).first()
    if db_swap:
        db_swap.status = new_status
        db.commit()
        db.refresh(db_swap)
    return db_swap

