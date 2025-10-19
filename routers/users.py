from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db_dependency
from models.user import User as UserModel
from schemas.common import User as UserSchema
from auth.security import get_password_hash
from sqlalchemy.exc import IntegrityError


router = APIRouter()

@router.get("/")
async def get_users(db: Session = Depends(get_db_dependency)):
    users = db.query(UserModel).all()
    return [u.to_dict() for u in users]

@router.get("/{user_id}/")
async def get_user(user_id: int, db: Session = Depends(get_db_dependency)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

@router.post("/")
async def create_user(user: UserSchema, db: Session = Depends(get_db_dependency)):
    # Pre-check unique constraints for clearer API errors
    existing_user = None
    existing_by_username = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if existing_by_username:
        existing_user = existing_by_username
    elif user.email:
        existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
        
    if existing_user:
        raise HTTPException(status_code=409, detail="Username or email already exists")
        
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
        # Fallback in case of race condition or other unique constraint
        raise HTTPException(status_code=409, detail="Username or email already exists")
    db.refresh(new_user)
    return new_user.to_dict()
