from typing import Optional
from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    user_id: int
    model_config = ConfigDict(from_attributes=True)
