from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as user_router
from .categories import router as categories_router
router = APIRouter(prefix="/v1")

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(categories_router)