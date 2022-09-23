from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    booking_id: int
    booking_expiration: datetime


class Reservation(ReservationBase):
    id: int
    created_at: datetime
    isActive: bool

    class Config:
        orm_mode = True


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(ReservationBase):
    pass


