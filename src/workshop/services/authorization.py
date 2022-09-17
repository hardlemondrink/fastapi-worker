from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.user import User


class AuthorizationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int,) -> tables.User:
        user = (
            self.session
            .query(tables.User)
            .filter_by(
                id=user_id, 
                isActive=True)
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='USER NOT FOUND')
        return user

    def create(self, user_data: User) -> tables.User:
        user = tables.User(**user_data.dict())
        user.isActive = True
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, user_id: int) -> tables.User:
        return self._get(user_id)

    def delete(self, user_id: int):
        user = self._get(user_id)
        user.isActive = False
        self.update(user_id=user_id, user_data=user)
        self.session.commit()

    def update(self, user_id: int, user_data: User) -> tables.User:
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user