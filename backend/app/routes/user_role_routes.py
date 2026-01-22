from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.user_role import UserRole
from app.schemas.user_role_schema import UserRoleResponse

router = APIRouter(prefix="/user-roles", tags=["User Roles"])

@router.get("/", response_model=List[UserRoleResponse])
def get_user_roles(db: Session = Depends(get_db)):
    return db.query(UserRole).all()
