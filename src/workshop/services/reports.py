import csv
from io import StringIO
from typing import Any

from fastapi import Depends

from ..models.booking import BookingCreate, Booking
from .booking import BookingService


class ReportsService:
    def __init__(self, booking_service: BookingService = Depends()):
        self.booking_service = booking_service

    def import_csv(self, user_id: int, file: Any):
        reader = csv.DictReader(
            (line.decode() for line in file),
            fieldnames=[
                'description',
                'address',
                'price',
                'city',
                'country',
                'phoneNumber'
            ]
        )

        books = []
        next(reader)
        for row in reader:
            book_data = BookingCreate.parse_obj(row)
            if book_data.description == '':
                book_data.description = None
            books.append(book_data)

        self.booking_service.create_many(
            user_id,
            books
        )

    def export_csv(self, user_id: int) -> Any:
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=[
                'description',
                'address',
                'price',
                'city',
                'country',
                'phoneNumber'
            ],
            extrasaction='ignore'
        )

        books = self.booking_service.get_list(user_id)

        writer.writeheader()

        for book in books:
            book_data = Booking.from_orm(book)
            writer.writerow(book_data.dict())

        output.seek(0)
        return output
