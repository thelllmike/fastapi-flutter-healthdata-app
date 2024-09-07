from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from crud.user_crud import create_user, get_user_by_email
from pydantic import BaseModel

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
        return {
            "message": "User already exists, logging in.",
            "status": "success",
            "user_id": existing_user.id  # Use `id` instead of `user_id`
        }
    
    new_user = create_user(db, email=user_data.email, name=user_data.name, profile_picture=user_data.profile_picture)
    return {
        "message": "New user created, logging in.",
        "status": "success",
        "user_id": new_user.id  # Use `id` instead of `user_id`
    }