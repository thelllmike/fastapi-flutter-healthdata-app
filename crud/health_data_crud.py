import json
from sqlalchemy.orm import Session
from models.health_data_model import HealthData
from schemas.health_data_schema import HealthDataCreate

# Create health data for a specific user
def create_health_data(db: Session, health_data: HealthDataCreate, user_id: int):
    db_health_data = HealthData(
        user_id=user_id,  # This comes from the authenticated user
        height=health_data.height,
        weight=health_data.weight,
        blood_type=health_data.blood_type,
        allergies=json.dumps(health_data.allergies),  # Serialize list to JSON
        medical_conditions=json.dumps(health_data.medical_conditions)  # Serialize list to JSON
    )
    db.add(db_health_data)
    db.commit()
    db.refresh(db_health_data)
    return db_health_data

# Get health data for a specific user
def get_health_data_by_user_id(db: Session, user_id: int):
    health_data = db.query(HealthData).filter(HealthData.user_id == user_id).first()
    if health_data:
        # Deserialize JSON strings into Python lists
        health_data.allergies = json.loads(health_data.allergies) if health_data.allergies else []
        health_data.medical_conditions = json.loads(health_data.medical_conditions) if health_data.medical_conditions else []
    return health_data