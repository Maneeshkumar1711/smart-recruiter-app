from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime | None

    class Config:
        orm_mode = True
