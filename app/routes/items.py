from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import item as item_schema
from app.crud import item as item_crud
from app.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=item_schema.ItemOut)
def create_item(item: item_schema.ItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return item_crud.create_item(db, item, owner_id=current_user.id)

@router.get("/", response_model=list[item_schema.ItemOut])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return item_crud.get_items(db, skip=skip, limit=limit)

@router.delete("/{item_id}", response_model=item_schema.ItemOut)
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = item_crud.get_item_by_id(db, item_id)
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found or unauthorized")
    return item_crud.delete_item(db, item_id)
