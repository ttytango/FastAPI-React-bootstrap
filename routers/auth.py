from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel


from auth.auth_endpoints import (
    get_current_active_user,
    fake_users_db,
    fake_hash_password,
    UserInDB,
)

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()



@router.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_active_user)):
    return current_user



@router.get("/status")
async def read_status():
    return {"status": "ok"}


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@router.post("/token/")
async def login_trailing(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login(form_data)  # support trailing slash

