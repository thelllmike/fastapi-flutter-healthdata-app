from sqlalchemy import Column, Integer, Float, String, ForeignKey, JSON
from db.database import Base
from sqlalchemy.orm import relationship

class HealthData(Base):
    __tablename__ = 'health_data'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    blood_type = Column(String(5), nullable=False)
    allergies = Column(JSON, nullable=True)
    medical_conditions = Column(JSON, nullable=True)

  