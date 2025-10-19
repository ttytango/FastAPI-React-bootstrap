import json
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db import Base
from another_service.schemas.todos import TodoOut
from typing import Dict, Any


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)    
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(255), index=True, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def to_schema(self):
        return TodoOut(id=self.id, title=self.title, description=self.description, completed=self.completed, user_id=self.user_id)
    
    
    def from_schema(self, schema: TodoOut):
        self.title = schema.title
        self.description = schema.description
        self.completed = schema.completed
        self.user_id = schema.user_id
        return self
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def from_json(self, json: str):
        self.from_dict(json.loads(json))
        return self