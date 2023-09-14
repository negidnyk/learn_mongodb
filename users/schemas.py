from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
# from sqlalchemy.sql import func
from datetime import datetime, time, timedelta
from uuid import UUID
from enum import Enum

# func.now()


class CreateUser(BaseModel):
    email: EmailStr
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "name": "John Doe",
                "password": "Qwerty123"
            }
        }


class UpdateUsername(BaseModel):
    username: str


class UserOut (BaseModel):
    id: int
    email: EmailStr
    username: str
    registered_at: datetime


class SortingOptions(str, Enum):
    registered_at = "registered_at"
    id = "_id"


class SortingDirections(int, Enum):
    asc = 1
    desc = -1
