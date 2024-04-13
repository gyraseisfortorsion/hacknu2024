from .base import Model, ReadModel, ReadNamedModel, ReadNamedModelShort
import datetime
import uuid
from typing import List, Optional
from dateutil.relativedelta import relativedelta

from pydantic import EmailStr, Field, root_validator, validator, ConfigDict, StringConstraints
from datetime import date

class CashbackBase(ReadModel):
    card_type_id: Optional[str] = None
    bank_id: Optional[str] = None
    is_qr: Optional[bool] = None
    title: Optional[str] = None
    description: Optional[str] = None
    reward: str
    reward_type_id: str
    min_payment: Optional[float] = None
    max_reward: Optional[str] = None
    category_id: str
    date_to: Optional[date] = None
    date_from: Optional[date] = None
    type_id: str
    recurrence_id: Optional[str] = None
    comments: Optional[str] = None
    special_requirements: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None

class CashbackRead(CashbackBase):
    
    pass

class CashbackCreate(CashbackBase):
    model_config = ConfigDict(from_attributes=True)
    pass

class CashbackUpdate(CashbackBase):
    model_config = ConfigDict(from_attributes=True)
    pass

