from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db_dependency
from models.user import User as UserModel
from schemas.common import User as UserSchema


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
    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=user.password,
        role=user.role.value if hasattr(user.role, "value") else user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.to_dict()

 

# async def create_user(user: User):
#     return {"user": user}

# async def update_user(user_id: int, user: User):
#     return {"user": user_id}

# async def delete_user(user_id: int):
#     return {"user": user_id}