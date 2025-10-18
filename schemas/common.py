from typing import Optional
from enum import Enum, IntEnum

from pydantic import BaseModel

class Status(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
     
class Role(str, Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"
    contributor = "contributor"
    viewer = "viewer"
    
class Permission(str, Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    role: Optional[Role] = Role.user
    
