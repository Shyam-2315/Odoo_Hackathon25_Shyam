from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class SwapStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    completed = "completed"

class Swap(Base):
    __tablename__ = "swaps"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)

    offered_by_id = Column(Integer, ForeignKey("users.id"))
    offered_to_id = Column(Integer, ForeignKey("users.id"))

    status = Column(Enum(SwapStatus), default=SwapStatus.pending)
    timestamp = Column(DateTime, default=datetime.utcnow)

    offered_by = relationship("User", foreign_keys=[offered_by_id], back_populates="swaps_offered")
    offered_to = relationship("User", foreign_keys=[offered_to_id], back_populates="swaps_received")
