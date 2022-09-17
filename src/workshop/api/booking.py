from typing import (List,
                    Optional)

from fastapi import (APIRouter,
                     Depends)

from ..models.booking import (BookingBase,
                              BookingCreate,
                              BookType,
                              Booking)
from ..services.booking import BookingService

router = APIRouter(
    prefix='/booking',
)


@router.get('/', response_model=List[BookingBase])
def get_opertaions(book_type: Optional[BookType] = None, service: BookingService = Depends()):
    return service.get_list(book_type=book_type)


@router.post('/', response_model=Booking)
def create_operation(book_data: BookingCreate, service: BookingService = Depends()):
    return service.create(book_data)


@router.get('/{book_id}', response_model=BookingBase)
def get_operation(book_id: int, service: BookingService = Depends()):
    return service.get(book_id)


@router.delete('/')
def delete_operation(book_id: int, service: BookingService = Depends()):
    return service.delete(book_id)


# @router.update('/{book_id}', response_model=BookingBase)
# def update_operation(book_id: int, service: BookingService = Depends()):
#     return service.update(book_id)