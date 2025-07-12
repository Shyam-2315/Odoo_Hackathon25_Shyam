from sqlalchemy.orm import Session
from app.models import item as item_model
from app.schemas import item as item_schema

def create_item(db: Session, item: item_schema.ItemCreate, owner_id: int):
    db_item = item_model.Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model.Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(item_model.Item).filter(item_model.Item.id == item_id).first()

def delete_item(db: Session, item_id: int):
    db_item = get_item_by_id(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item