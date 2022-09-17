from typing import List, Optional

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.booking import BookingCreate, BookType, BookingUpdate
from ..services.pictures import PictureService


class BookingService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, book_id: int) -> tables.Booking:
        book = (
            self.session
                .query(tables.Booking)
                .filter_by(id=book_id)
                .first()
        )
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        # pictures = PictureService.get_pictures(self, book_id=book.id)
        # for pic in pictures:
        #     book.pics.append(pic)

        return book

    def get_list(self, book_type: Optional[BookType] = None) -> List[tables.Booking]:
        query = self.session.query(tables.Booking)
        if type:
            query = query.filter_by(book_type=book_type)
        books = query.all()
        return books

    def create(self, book_data: BookingCreate) -> tables.Booking:
        book = tables.Booking(**book_data.dict())
        self.session.add(book)
        self.session.commit()
        return book

    def get(self, book_id: int) -> tables.Booking:
        return self._get(book_id)

    def delete(self, book_id: int):
        book = self._get(book_id)
        self.session.delete(book)
        self.session.commit()

    def update(self, book_id: int, book_data: BookingUpdate) -> tables.Booking:
        book = self._get(book_id)
        for field, value in book_data:
            setattr(book, field, value)
        self.session.commit()
        return book
