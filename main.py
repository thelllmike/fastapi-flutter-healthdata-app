from fastapi import FastAPI
from db.database import engine  # Import engine from db.database
from models import user_model, health_data_model  # Import your models
from api import users, health_data, token  # Import your API routers including token
from fastapi.middleware.cors import CORSMiddleware  # Import CORS Middleware

# Create the tables in the database if they don't exist
user_model.Base.metadata.create_all(bind=engine)
health_data_model.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Configure CORS to allow your frontend app to communicate with the backend
origins = [
    "http://localhost",            # Add your local development frontend URL
    "http://localhost:3000",       # Example React/Vue/Angular frontend running on port 3000
    "http://localhost:8000",       # FastAPI backend
    "http://127.0.0.1",            # Allow local IP addresses as well
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Allows listed origins to access the backend
    allow_credentials=True,        # Allows cookies and authentication headers
    allow_methods=["*"],           # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],           # Allows all headers (Authorization, Content-Type, etc.)
)

# Include the routers from your API

app.include_router(health_data.router, prefix="/health_data", tags=["Health Data"])  # Health data endpoints
app.include_router(token.router)
app.include_router(users.router, prefix="/auth", tags=["Auth"])
 # Add token router

# Define a root endpoint to check if the API is running
@app.get("/")
async def root():
    return {"message": "Welcome to the Health Data API"}