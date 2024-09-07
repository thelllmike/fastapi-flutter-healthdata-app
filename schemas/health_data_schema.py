from pydantic import BaseModel
from typing import List, Optional

# Schema for creating health data (no user_id here)
class HealthDataCreate(BaseModel):
    height: float
    weight: float
    blood_type: str
    allergies: Optional[List[str]] = []
    medical_conditions: Optional[List[str]] = []

    class Config:
        from_attributes = True  # For Pydantic v2

# Schema for outputting health data (with user_id for responses)
class HealthDataOut(BaseModel):
    id: int
    user_id: int
    height: float
    weight: float
    blood_type: str
    allergies: List[str] = []
    medical_conditions: List[str] = []

    class Config:
        from_attributes = True