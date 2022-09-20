from fastapi import APIRouter
from .healthcheck import router as healthcheck_router
from .booking import router as booking_router
from .auth import router as auth_router
from .reports import router as reports_router


router = APIRouter()
router.include_router(healthcheck_router)
router.include_router(auth_router)
router.include_router(booking_router)
router.include_router(reports_router)
