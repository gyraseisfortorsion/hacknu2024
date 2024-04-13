from .base import ServiceBase
from fastapi import Depends
from core import get_db
from models import User
from utils import hash_password
from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder
from schemas import (
    UserCreate,
    UserUpdate,
    UserRead,
)
class UserService(ServiceBase[User, UserCreate, UserUpdate]):

    def create(self, db: Session, body: UserCreate):
        # then create user
        body.password_hash = hash_password(body.password_hash)
        user = User(**body.dict()) 
        # user.password_hash = hash_password(body.password_hash)
        db.add(user)
        db.commit()
        return user


    def get_user_by_email(self, email: str, db: Session):
        return db.query(User).filter(User.email == email).first()
    
user_service = UserService(User)
        
        