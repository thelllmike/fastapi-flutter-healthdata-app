from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    name: str = None
    profile_picture: str = None

class UserOut(BaseModel):
    id: int
    email: str
    name: str = None
    profile_picture: str = None

    class Config:
        orm_mode = True