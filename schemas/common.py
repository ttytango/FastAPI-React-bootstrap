import re
from typing import Optional
from enum import Enum, IntEnum

from pydantic import BaseModel, Field, EmailStr, field_validator, FieldValidationInfo

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
    username: str = Field(min_length=3, max_length=50, pattern=r"^[A-Za-z0-9_.-]+$",  description="3–50 chars; letters, numbers, _, ., -")
    email: EmailStr
    password: str = Field(min_length=8, max_length=128, description="Password must be between 8 and 128 characters")
    role: Optional[Role] = Role.user
    

    @field_validator('username', mode='before')
    @classmethod
    def normalize_and_validate_username(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError('Username must be a string')
        u = v.strip()
        if ' ' in u:
            raise ValueError('Username cannot contain spaces')
        _ALLOWED = re.compile(r'^[A-Za-z0-9_.-]+$')

        if not _ALLOWED.fullmatch(u):
            raise ValueError('Username may only contain letters, numbers, underscore (_), dot (.), and hyphen (-)')
        return u