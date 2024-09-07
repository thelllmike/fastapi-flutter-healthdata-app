from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import health_data_schema
from crud import health_data_crud
from db.database import get_db
from core.security import get_current_user

router = APIRouter(prefix="/health_data", tags=["Health Data"])

@router.post("/", response_model=health_data_schema.HealthDataOut)
def create_health_data(
    health_data: health_data_schema.HealthDataCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return health_data_crud.create_health_data(db=db, health_data=health_data, user_id=current_user)

@router.get("/{customer_id}", response_model=health_data_schema.HealthDataOut)
def get_health_data(customer_id: int, db: Session = Depends(get_db)):
    return health_data_crud.get_health_data_by_user_id(db=db, user_id=customer_id)