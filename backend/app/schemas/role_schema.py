from pydantic import BaseModel
from datetime import datetime

class RoleResponse(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: datetime | None

    class Config:
        orm_mode = True
