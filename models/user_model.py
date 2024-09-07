from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Add password field if needed
    name = Column(String(255), nullable=True)
    profile_picture = Column(String(255), nullable=True)