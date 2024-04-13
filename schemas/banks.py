from .base import Model, ReadModel, ReadNamedModel, ReadNamedModelShort
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints

class BankRead(ReadNamedModel):
    pass

class BankCreate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]

class BankUpdate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]