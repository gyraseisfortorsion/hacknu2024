from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core import get_db
from schemas import LoginForm, CashbackCreate
from services import cashbacks_service

router = APIRouter(prefix = '/reward_types', tags=["HackNU2024", "RewardTypes"])

@router.get("")
def get_cashbacks(db: Session = Depends(get_db)):
    return cashbacks_service.get_reward_types(db)