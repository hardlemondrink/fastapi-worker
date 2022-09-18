from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class BookType(str, Enum):
    # Сдать в аренду
    TO_RENT = 'to_rent'
    # Снять в аренду
    RENT = 'rent'


class BookingBase(BaseModel):
    created_at: datetime
    description: Optional[str]
    book_type: BookType
    address: str
    price: float
    country: str
    city: str
    phoneNumber: str


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass
