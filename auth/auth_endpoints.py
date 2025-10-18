from fastapi import Depends, HTTPException, status

from auth.schema import User, UserInDB, fake_users_db, fake_hash_password, fake_decode_token, oauth2_scheme


def fake_decode_token(token):
    return {"sub": "user"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if current_user.get("disabled"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user



