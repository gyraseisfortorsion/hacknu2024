from .base import Model, ReadModel, ReadNamedModel, ReadNamedModelShort
from .banks import BankRead
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints

class CardTypeRead(ReadNamedModel):
    bank: BankRead
    is_virtual: bool
    payment_system: str
    card_type: str

class CardTypeCreate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]
    bank_id: str
    is_virtual: bool
    payment_system: str
    card_type: str

class CardTypeUpdate(ReadModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: Optional[str]
    name_ru: Optional[str]
    name_kz: Optional[str]
    bank_id: Optional[str]
    is_virtual: Optional[bool]
    payment_system: Optional[str]
    card_type: Optional[str]