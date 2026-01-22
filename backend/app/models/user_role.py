from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="RESTRICT"))
    assigned_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")
