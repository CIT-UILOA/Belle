from pydantic import BaseModel


# Base schema for shared fields
class UserBase(BaseModel):
    name: str


# For creating new users (input)
class UserCreate(UserBase):
    pass


# For returning users to clients (output)
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True  # allows SQLAlchemy model → Pydantic conversion
