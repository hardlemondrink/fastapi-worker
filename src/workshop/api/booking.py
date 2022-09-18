from typing import (List,
                    Optional)

from fastapi import (APIRouter,
                     Depends,
                     status)
from fastapi.openapi.models import Response

from ..models.auth import User
from ..models.booking import (BookingCreate,
                              BookType,
                              Booking, BookingUpdate)
from ..services.auth import get_current_user
from ..services.booking import BookingService

router = APIRouter(
    prefix='/booking',
)


@router.get('/', response_model=List[Booking])
def get_books(book_type: Optional[BookType] = None,
              service: BookingService = Depends(),
              user: User = Depends(get_current_user)):
    return service.get_list(user_id=user.id, book_type=book_type)


@router.post('/', response_model=Booking)
def create_book(book_data: BookingCreate,
                service: BookingService = Depends(),
                user: User = Depends(get_current_user)):
    return service.create(user_id=user.id, book_data=book_data)


@router.get('/{book_id}', response_model=Booking)
def get_book(book_id: int,
             service: BookingService = Depends(),
             user: User = Depends(get_current_user)):
    return service.get(user_id=user.id, book_id=book_id)


@router.delete('/{book_id}')
def delete_book(book_id: int,
                service: BookingService = Depends(),
                user: User = Depends(get_current_user)):
    service.delete(user_id=user.id, book_id=book_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{book_id}', response_model=Booking)
def update_book(book_id: int,
                book_data: BookingUpdate,
                service: BookingService = Depends(),
                user: User = Depends(get_current_user)):
    return service.update(user_id=user.id, book_id=book_id, book_data=book_data)