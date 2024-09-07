import json
from sqlalchemy import Column, Float, Integer, String, Text
from db.database import Base

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    blood_type = Column(String(3), nullable=False)
    allergies = Column(Text, nullable=True)  # Stored as JSON string
    medical_conditions = Column(Text, nullable=True)  # Stored as JSON string

    # Method to deserialize allergies field
    def get_allergies(self):
        return json.loads(self.allergies) if self.allergies else []

    # Method to deserialize medical_conditions field
    def get_medical_conditions(self):
        return json.loads(self.medical_conditions) if self.medical_conditions else []