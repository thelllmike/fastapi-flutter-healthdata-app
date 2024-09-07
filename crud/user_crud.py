import uuid
from sqlalchemy.orm import Session
from models.user_model import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

from models.user_model import User
from sqlalchemy.orm import Session

def create_user(db: Session, email: str, name: str, profile_picture: str):
    # Create a new user object without user_id
    db_user = User(email=email, name=name, profile_picture=profile_picture)
    
    # Add the new user to the session and commit
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()