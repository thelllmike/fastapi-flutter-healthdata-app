from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.health_data_model import HealthData
from models.user_model import User
from schemas import health_data_schema
from crud import health_data_crud, user_crud
from db.database import get_db
from core.security import get_current_user  # Import the get_current_user function

router = APIRouter()

# Create health data for the current authenticated user
@router.post("/", response_model=health_data_schema.HealthDataOut)
def create_health_data(
    health_data: health_data_schema.HealthDataCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)  # Ensure the user is authenticated
):
    # Assuming get_current_user returns the email, fetch the user from DB
    user = user_crud.get_user_by_email(db, current_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Create health data for the authenticated user
    return health_data_crud.create_health_data(db=db, health_data=health_data, user_id=user.id)
# Get health data for a specific user (only if the current user is the same as the requested user)
@router.get("/{user_id}", response_model=health_data_schema.HealthDataOut)
def get_health_data(user_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    # Ensure the current user can only access their own health data
    if current_user != str(user_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    # Fetch health data for the user
    health_data = health_data_crud.get_health_data_by_user_id(db=db, user_id=user_id)
    if not health_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Health data not found")

    return health_data