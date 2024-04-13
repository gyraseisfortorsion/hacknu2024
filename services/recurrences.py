from .base import ServiceBase
from fastapi import Depends
from core import get_db
from models import Recurrence, RecurrenceType
from utils import hash_password
from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder
from schemas import (
    RecurrenceRead, 
    RecurrenceCreate,
    RecurrenceUpdate,
    RecurrenceTypeRead, 
    RecurrenceTypeCreate,
    RecurrenceTypeUpdate,
)

class RecurrenceService(ServiceBase[Recurrence, RecurrenceCreate, RecurrenceUpdate]):
    def get_all(self, db: Session):
        return db.query(self.model).all()
    
    def get_types(self, db: Session):
        return db.query(RecurrenceType).all()
    
    # def create(self, db: Session, obj_in: BankCreate):
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

recurrences_service = RecurrenceService(Recurrence)