from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from crud.user_crud import create_user, get_user_by_email
from pydantic import BaseModel
from api.token import create_access_token  # Assuming your token creation logic is here
from typing import Dict
from datetime import timedelta

router = APIRouter()

# Pydantic schema for Google login request
class GoogleLoginRequest(BaseModel):
    email: str
    name: str
    profile_picture: str

@router.post("/google_login")
async def google_login(user_data: GoogleLoginRequest, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    
    if existing_user:
        access_token = create_access_token(data={"sub": existing_user.email})  # Create token
        print(f"Generated token: {access_token}")  # Debugging
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "message": "User already exists, logging in.",
            "status": "success",
            "user_id": existing_user.id
        }
    
    # Create new user logic
    new_user = create_user(db, email=user_data.email, name=user_data.name, profile_picture=user_data.profile_picture)
    access_token = create_access_token(data={"sub": new_user.email})  # Create token
    print(f"Generated token: {access_token}")  # Debugging
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "New user created, logging in.",
        "status": "success",
        "user_id": new_user.id
    }