from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    points = Column(Integer, default=100)

    items = relationship("Item", back_populates="owner")
    swaps_offered = relationship("Swap", back_populates="offered_by", foreign_keys='Swap.offered_by_id')
    swaps_received = relationship("Swap", back_populates="offered_to", foreign_keys='Swap.offered_to_id')
