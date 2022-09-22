from typing import List, Optional

from fastapi import APIRouter, Depends

from ..models.auth import User
from ..models.reservations import Reservation, ReservationCreate
from ..services.auth import get_current_user
from ..services.reservations import ReservationService

router = APIRouter(
    prefix='/reservations',
)


@router.get('/', response_model=List[Reservation])
def get_reservations(reservation_id: Optional[int] = None,
                     service: ReservationService = Depends(),
                     user: User = Depends(get_current_user)):
    return service.get_reservations(user.id, reservation_id)


@router.post('/', response_model=ReservationCreate)
def create_reservation(reservation_data: ReservationCreate,
                       service: ReservationService = Depends(),
                       user: User = Depends(get_current_user)):
    return service.create_reservation(user.id, reservation_data)
