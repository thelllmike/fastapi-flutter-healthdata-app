from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import timedelta, datetime

# Secret key to encode/decode the JWT token
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

# Define a model for the token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Define the route to get the token
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Add your authentication logic here
    user = {"username": form_data.username}  # Replace with actual user lookup
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = jwt.encode({"sub": user["username"], "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}