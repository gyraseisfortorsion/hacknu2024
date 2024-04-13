from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, CashbackCreate
from services import cashbacks_service

router = APIRouter(prefix = '/cashbacks', tags=["HackNU2024"])

@router.get("")
def get_cashbacks(db: Session = Depends(get_db)):
    return cashbacks_service.get(db)

@router.get("/{cashback_id}")
def get_cashback(cashback_id: str, db: Session = Depends(get_db)):
    return cashbacks_service.get_by_id(db, cashback_id)

@router.post("")
def create_cashback(body: CashbackCreate, db: Session = Depends(get_db)):
    return cashbacks_service.create(db, body)

@router.get("")
def get_cashbacks_with_filters(
    db: Session = Depends(get_db),
    payment: int = None,
    card_type_id: str = None,
    bank_id: str = None,
    is_qr: bool = None,
    reward: str = None,
    reward_type: str = None,
    min_payment: int = None,
    max_reward: int = None,
    category_id: str = None,
    date_to: str = None,
    city: str = None,
    company_name: str = None
):
    return cashbacks_service.get_with_filters(
        db, payment, card_type_id, bank_id, is_qr, reward, reward_type, min_payment, max_reward, category_id, date_to, city, company_name
    )