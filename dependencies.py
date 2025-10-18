from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Generator

from db import get_db


def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    return token


def get_db_dependency(db: Session = Depends(get_db)) -> Generator[Session, None, None]:
    yield db