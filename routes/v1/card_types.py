from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, CardTypeCreate
from services import card_type_service

router = APIRouter(prefix = '/card_types', tags=["HackNU2024", "CardTypes"])

@router.get("")
def get_card_type(db: Session = Depends(get_db)):
    return card_type_service.get(db)

@router.get("/{card_type_id}")
def get_card_type(card_type_id: str, db: Session = Depends(get_db)):
    return card_type_service.get_by_id(db, card_type_id)

@router.post("")
def create_card_type(body: CardTypeCreate, db: Session = Depends(get_db)):
    return card_type_service.create(db, body)