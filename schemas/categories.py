from .base import Model, ReadModel, ReadNamedModel, ReadNamedModelShort
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints

class CategoryRead(ReadNamedModel):
    pass

class CategoryCreate(Model):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]

class CategoryUpdate(Model):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]

