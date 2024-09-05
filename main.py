from fastapi import FastAPI
from app.db.database import engine
from app.models import user_model, health_data_model
from app.api import users, health_data

# Create tables
user_model.Base.metadata.create_all(bind=engine)
health_data_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(health_data.router)