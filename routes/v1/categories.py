from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, CategoryCreate
from services import categories_service

router = APIRouter(prefix = '/categories', tags=["HackNU2024"])

@router.get("")
def get_categories(db: Session = Depends(get_db)):
    return categories_service.get_categories(db)

@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    return categories_service.get_category(category_id, db)

@router.post("")
def create_category(body: CategoryCreate, db: Session = Depends(get_db)):
    return categories_service.create(db, body)