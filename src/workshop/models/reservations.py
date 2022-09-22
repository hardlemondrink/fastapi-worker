from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReservationCreate(BaseModel):
    booking_id: int
    created_at: datetime


class Reservation(BaseModel):
    id: int
    booking_id: int
    created_at: datetime



