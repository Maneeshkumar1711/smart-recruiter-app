from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.role import Role
from app.schemas.role_schema import RoleResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=List[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()
