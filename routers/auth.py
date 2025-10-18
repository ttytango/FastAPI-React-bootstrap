from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel


from auth.security import (
    get_current_active_user,
    get_user_by_username,
    verify_password,
    create_access_token,
)
from db import get_db
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()



@router.get("/users/me")
async def read_users_me(current_user = Depends(get_current_active_user)):
    return current_user



@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token/")
async def login_trailing(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login(form_data, db)  # support trailing slash

