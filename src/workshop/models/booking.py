from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel

from ..models.pictures import Picture


class BookType(str, Enum):
    # Сдать в аренду
    TO_RENT = 'to_rent'
    # Снять в аренду
    RENT = 'rent'


class BookingBase(BaseModel):
    id: int
    created_at: datetime
    description: Optional[str]
    book_type: BookType
    address: str
    # pics: List[Picture]

    class Config:
        orm_mode = True


class Booking(BookingBase):
    pass


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass