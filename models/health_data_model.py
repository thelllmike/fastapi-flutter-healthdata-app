from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    height = Column(Float)
    weight = Column(Float)
    blood_type = Column(String)
    allergies = Column(String)
    medical_conditions = Column(String)

    customer = relationship("User", back_populates="health_data")