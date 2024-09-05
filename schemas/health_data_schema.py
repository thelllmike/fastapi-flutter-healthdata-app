from pydantic import BaseModel

class HealthDataCreate(BaseModel):
    height: float
    weight: float
    blood_type: str
    allergies: list[str] = []
    medical_conditions: list[str] = []

class HealthDataOut(BaseModel):
    id: int
    height: float
    weight: float
    blood_type: str

    class Config:
        orm_mode = True