from fastapi import Depends

from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session


class PictureService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_pictures(self, book_id: int) -> tables.Pictures:
        pictures = (
            self.session
                .query(tables.Pictures)
                .filter_by(book_id=book_id)
        )
        return pictures


