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
# from ..services.pictures import PictureService


class BookingService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self,
             user_id: int,
             book_id: int) -> tables.Booking:
        book = (
            self.session
                .query(tables.Booking)
                .filter_by(id=book_id,
                           user_id=user_id)
                .first()
        )
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        # pictures = PictureService.get_pictures(self, book_id=book.id)
        # for pic in pictures:
        #     book.pics.append(pic)

        return book

    def get_list(self,
                 user_id: int,
                 book_type: Optional[BookType] = None) -> List[tables.Booking]:
        query = (
            self.session
            .query(tables.Booking)
            .filter_by(user_id=user_id)
        )
        if book_type:
            query = query.filter_by(book_type=book_type)
        books = query.all()
        return books

    def create_many(self, user_id: int, books_data: List[BookingCreate]) -> List[tables.Booking]:
        books = [
            tables.Booking(
                **book_data.dict(),
                user_id=user_id
            )
            for book_data in books_data
        ]
        self.session.add_all(books)
        self.session.commit()
        return books

    def create(self,
               user_id: int,
               book_data: BookingCreate) -> tables.Booking:

        book = tables.Booking(
            **book_data.dict(),
            user_id=user_id,
        )
        self.session.add(book)
        self.session.commit()
        return book

    def get(self,
            user_id: int,
            book_id: int) -> tables.Booking:
        return self._get(user_id, book_id)

    def delete(self,
               user_id: int,
               book_id: int):
        book = self._get(user_id, book_id)
        self.session.delete(book)
        self.session.commit()

    def update(self,
               user_id: int,
               book_id: int,
               book_data: BookingUpdate) -> tables.Booking:
        book = self._get(user_id, book_id)
        for field, value in book_data:
            setattr(book, field, value)
        self.session.commit()
        return book
