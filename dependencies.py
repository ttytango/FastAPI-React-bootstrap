from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Generator
from jose import JWTError, jwt

from db import get_db
from config import get_settings
from models.user import User as UserModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db_dependency(db: Session = Depends(get_db)) -> Generator[Session, None, None]:
    yield db


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db_dependency),
):
    settings = get_settings()
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user is None:
        raise credentials_exception
    return user