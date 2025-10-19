import json
from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from db import Base
from datetime import datetime
from sqlalchemy.types import DateTime
from schemas.common import Role, User as UserSchema
from typing import Dict, Any

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(254), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String(16), nullable=False, default=Role.user.value)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email}, role={self.role})"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def from_dict(self, data: Dict[str, Any]):
        self.username = data.get("username")
        self.email = data.get("email")
        self.role = data.get("role")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        return self

    def to_json(self):
        return json.dumps(self.to_dict())

    def from_json(self, data: str):
        self.from_dict(json.loads(data))
        return self
    
    
    def to_schema(self):
        return UserSchema(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            role=self.role,
        )
    
    def from_schema(self, schema: UserSchema):
        self.id = schema.id
        self.username = schema.username
        self.email = schema.email
        self.role = schema.role
        return self
