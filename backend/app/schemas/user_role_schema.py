from pydantic import BaseModel
from datetime import datetime

class UserRoleResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    assigned_at: datetime | None

    class Config:
        orm_mode = True
