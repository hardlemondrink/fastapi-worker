import datetime

from fastapi import (
    Depends,
    HTTPException,
    status
)

from typing import Optional, List
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.reservations import ReservationCreate, Reservation


class ReservationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self,
             user_id: int,
             reservation_id: int = None):
        query = (
            self.session
            .query(tables.Reservation)
            .filter_by(user_id=user_id,
                       isActive=True)
        )
        if reservation_id:
            query = query.filter_by(id=reservation_id)

        if not query:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return query.all()

    def create(self,
               user_id: int,
               reservation_data: ReservationCreate) -> tables.Reservation:

        reservation = tables.Reservation(
            **reservation_data.dict(),
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            isActive=True
        )
        self.session.add(reservation)
        self.session.commit()
        return reservation

    def get(self,
            user_id: int,
            reservation_id: Optional[int] = None) -> List[tables.Reservation]:
        return self._get(user_id, reservation_id)

    def delete(self,
               user_id: int,
               reservation_id: int):
        reservation = self._get(user_id, reservation_id)
        self.session.delete(reservation)
        self.session.commit()

