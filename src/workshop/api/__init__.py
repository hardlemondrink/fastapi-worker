from fastapi import APIRouter
from .operations import router as opertaions_router
from .booking import router as booking_router


router = APIRouter()
router.include_router(opertaions_router)
router.include_router(booking_router)

