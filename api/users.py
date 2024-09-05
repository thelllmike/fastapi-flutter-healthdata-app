from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.crud import user_crud
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=user_schema.UserOut)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=user_schema.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user(db=db, user_id=user_id)