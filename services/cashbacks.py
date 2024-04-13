from .base import ServiceBase
from fastapi import Depends
from core import get_db
from models import Cashback, CashbackType, RewardType
from utils import hash_password
from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder
from schemas import (
    CashbackRead, 
    CashbackCreate,
    CashbackUpdate
)

class CashbackService(ServiceBase[Cashback, CashbackCreate, CashbackUpdate]):
    def get_all(self, db: Session):
        return db.query(self.model).all()
    
    def get_with_filters(self, db: Session, payment, card_type_id, bank_id, is_qr, reward, reward_type, min_payment, max_reward, category_id, date_to, city, company_name):
        query = db.query(self.model)
        if payment:
            query = query.filter(self.model.min_payment <= payment)
        if card_type_id:
            query = query.filter(self.model.card_type_id == card_type_id)
        if bank_id:
            query = query.filter(self.model.bank_id == bank_id)
        if is_qr:
            query = query.filter(self.model.is_qr == is_qr)
        if reward:
            query = query.filter(self.model.reward == reward)
        if reward_type:
            query = query.filter(self.model.reward_type == reward_type)
        if min_payment:
            query = query.filter(self.model.min_payment == min_payment)
        if max_reward:
            query = query.filter(self.model.reward <= max_reward)
        if category_id:
            query = query.filter(self.model.category_id == category_id)
        if date_to:
            query = query.filter(self.model.date_to == date_to)
        if city:
            query = query.filter(self.model.city == city)
        if company_name:
            query = query.filter(self.model.company_name == company_name)

        calculated_cashback = []

        for i in query.all():

            cashback_temp = i

            if i.reward_type == 'percentage':
                cashback_temp.reward = float(i.reward) * payment
            else:
                cashback_temp.reward = float(i.reward)
            calculated_cashback.append(cashback_temp)

        calculated_cashback.sort(reverse=True)
        return calculated_cashback
    
    # def create(self, db: Session, obj_in: BankCreate):
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def get_cashback_types(self, db: Session):
        return db.query(CashbackType).all()
    
    def get_reward_types(self, db: Session):
        return db.query(RewardType).all()

cashbacks_service = CashbackService(Cashback)