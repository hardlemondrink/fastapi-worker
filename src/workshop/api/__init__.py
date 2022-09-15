from fastapi import APIRouter
from .operations import router as opertaions_router


router = APIRouter()
router.include_router(opertaions_router)
