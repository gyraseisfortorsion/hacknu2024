from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as user_router
from .categories import router as categories_router
from .banks import router as banks_router
from .card_types import router as card_types_router
from .cashbacks import router as cashbacks_router
from .cashback_types import router as cashback_types_router
from .reward_types import router as reward_types_router

router = APIRouter(prefix="/v1")

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(categories_router)
router.include_router(banks_router)
router.include_router(card_types_router)
router.include_router(cashbacks_router)
router.include_router(cashback_types_router)
router.include_router(reward_types_router)