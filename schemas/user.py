from .base import Model, ReadModel
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints


class UserRead(ReadModel):

    firstname: str
    surname: str
    email: EmailStr
    phone_number: str


class UserCreate(Model):
    model_config = ConfigDict(from_attributes=True)

    firstname: str
    surname: str
    email: EmailStr
    password_hash: str
    phone_number: str

class UserUpdate(Model):
    model_config = ConfigDict(from_attributes=True)
    
    role: Optional[int]
    email: Optional[EmailStr]
    password: Optional[str]
    phone_number: Optional[str]
