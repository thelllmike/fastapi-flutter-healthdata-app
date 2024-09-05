from sqlalchemy.orm import Session
from app.models.health_data_model import HealthData
from app.schemas.health_data_schema import HealthDataCreate

def create_health_data(db: Session, health_data: HealthDataCreate, user_id: int):
    db_health_data = HealthData(**health_data.dict(), customer_id=user_id)
    db.add(db_health_data)
    db.commit()
    db.refresh(db_health_data)
    return db_health_data

def get_health_data_by_user_id(db: Session, user_id: int):
    return db.query(HealthData).filter(HealthData.customer_id == user_id).first()