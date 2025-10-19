from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import Depends
from config import configure, get_settings 
from models.user import User as UserModel
from fastapi.exceptions import HTTPException
from dependencies import get_db_dependency, get_current_user
from another_service.schemas.todos import TodoCreate, TodoOut
from contextlib import asynccontextmanager
from another_service.models.todos import Todo
from db import setup_database, get_engine, Base
import another_service.models.todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure()
    settings = get_settings()
    setup_database(settings.database_url)
    Base.metadata.create_all(bind=get_engine())
    yield

app = FastAPI(title="Another API", lifespan=lifespan, dependencies=[Depends(get_current_user)])

configure()
settings = get_settings()


@app.get("/ping")
async def ping():
    return {"ok": True, "env": settings.environment}



@app.post("/todo", response_model=TodoOut)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db_dependency), user: UserModel = Depends(get_current_user)):
    print("DEBUG: user", user)
    new_todo = Todo(title=todo.title, description=todo.description, completed=todo.completed, user_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo.to_schema()


@app.get("/todo/{todo_id}", response_model=TodoOut)
async def get_todo(
        todo_id: int, 
        db: Session = Depends(get_db_dependency), 
        user: UserModel = Depends(get_current_user)
    ):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo.to_schema()