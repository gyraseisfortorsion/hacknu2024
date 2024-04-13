from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, BankCreate
from services import banks_service

router = APIRouter(prefix = '/banks', tags=["HackNU2024", "Banks"])

@router.get("")
def get_banks(db: Session = Depends(get_db)):
    return banks_service.get_all(db)

@router.get("/{bank_id}")
def get_bank(bank_id: str, db: Session = Depends(get_db)):
    return banks_service.get_by_id(db, bank_id)

@router.post("")
def create_bank(body: BankCreate, db: Session = Depends(get_db)):
    return banks_service.create(db, body)