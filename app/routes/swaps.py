from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import swap as swap_schema
from app.crud import swap as swap_crud
from app.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/swaps", tags=["Swaps"])

@router.post("/", response_model=swap_schema.SwapOut)
def create_swap(swap: swap_schema.SwapCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return swap_crud.create_swap(db, swap, offered_by_id=current_user.id)

@router.get("/", response_model=list[swap_schema.SwapOut])
def get_user_swaps(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return swap_crud.get_swaps_for_user(db, current_user.id)

@router.put("/{swap_id}/status", response_model=swap_schema.SwapOut)
def update_status(swap_id: int, new_status: swap_schema.SwapStatus, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    swap = swap_crud.update_swap_status(db, swap_id, new_status)
    if not swap:
        raise HTTPException(status_code=404, detail="Swap not found")
    return swap
