from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, RecurrenceCreate
from services import recurrences_service

router = APIRouter(prefix = '/categories', tags=["HackNU2024", "Categories"])

@router.get("")
def get_all(db: Session = Depends(get_db)):
    return recurrences_service.get_all(db)

@router.get("/types")
def get_types(db: Session = Depends(get_db)):
    return recurrences_service.get_types(db)

@router.get("/{recurrence_id}")
def get_by_id(recurrence_id: str, db: Session = Depends(get_db)):
    return recurrences_service.get_by_id(db, recurrence_id)

@router.post("")
def create_category(body: RecurrenceCreate, db: Session = Depends(get_db)):
    return recurrences_service.create(db, body)

# @router.post("/parse", tags=["HackNU2024"])
# def parse_categories(db: Session = Depends(get_db)):
#     return categories_service.parse_categories(db)