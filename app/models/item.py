from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class ItemStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    size = Column(String)
    condition = Column(String)
    tags = Column(String)  
    image_url = Column(String)
    is_available = Column(Boolean, default=True)
    status = Column(Enum(ItemStatus), default=ItemStatus.pending)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")
