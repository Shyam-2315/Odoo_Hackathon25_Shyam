from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

class SwapType(str, enum.Enum):
    swap = "swap"
    redeem = "redeem"

class SwapStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Swap(Base):
    __tablename__ = "swaps"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    requester_id = Column(Integer, ForeignKey("users.id"))
    type = Column(Enum(SwapType))
    status = Column(Enum(SwapStatus), default=SwapStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)

    item = relationship("Item")
    requester = relationship("User")
