from .base import Model, ReadModel, ReadNamedModel, ReadNamedModelShort
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints

class RecurrenceTypeRead(ReadNamedModelShort):
    pass

class RecurrenceTypeCreate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]

class RecurrenceTypeUpdate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]

class RecurrenceRead(ReadModel):
    type: RecurrenceTypeRead
    active_on: Optional[str]

class RecurrenceCreate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    type_id: str
    active_on: Optional[str]

class RecurrenceUpdate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    type_id: Optional[str]
    active_on: Optional[str]
