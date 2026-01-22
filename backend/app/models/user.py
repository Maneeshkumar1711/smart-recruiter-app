from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    is_active = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    roles = relationship("UserRole", back_populates="user")
    creator = relationship("User", remote_side=[id])
