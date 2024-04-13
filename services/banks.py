from .base import ServiceBase
from fastapi import Depends
from core import get_db
from models import Bank
from utils import hash_password
from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder
from schemas import (
    BankRead, 
    BankCreate,
    BankUpdate
)

class BankService(ServiceBase[Bank, BankCreate, BankUpdate]):
    def get_all(self, db: Session):
        return db.query(self.model).all()
    
    # def create(self, db: Session, obj_in: BankCreate):
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

banks_service = BankService(Bank)