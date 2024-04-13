from .base import ServiceBase
from fastapi import Depends
from core import get_db
from models import CashbackCategory
from utils import hash_password
from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder
from schemas import (
    CategoryRead,
    CategoryCreate,
    CategoryUpdate
)

class CategoryService(ServiceBase[CashbackCategory, CategoryCreate, CategoryUpdate]):
    def get_categories(self, db: Session):
        return db.query(CashbackCategory).all()
    
    def get_category(self, category_id: int, db: Session):
        return db.query(CashbackCategory).filter(CashbackCategory.id == category_id).first()
    
    def create(self, db: Session, body: CategoryCreate):
        category = CashbackCategory(**body.dict())
        db.add(category)
        db.commit()
        return category
    
categories_service = CategoryService(CashbackCategory)
    