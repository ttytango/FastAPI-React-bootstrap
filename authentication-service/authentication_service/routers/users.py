from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db import get_db
from models.user import User as UserModel
from schemas.common import User as UserSchema
from authentication_service.auth.security import get_password_hash


router = APIRouter()


@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return [u.to_dict() for u in users]


@router.get("/{user_id}/")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()


@router.post("/")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_by_username = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_by_username:
        raise HTTPException(status_code=409, detail="Username already exists")
    if user.email:
        existing_by_email = db.query(UserModel).filter(UserModel.email == user.email).first()
        if existing_by_email:
            raise HTTPException(status_code=409, detail="Email already exists")

    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        role=user.role.value if hasattr(user.role, "value") else user.role,
    )
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username or email already exists")
    db.refresh(new_user)
    return new_user.to_dict()


