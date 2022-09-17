from pydantic import BaseModel


class Picture(BaseModel):
    id: int
    path: str
    booking_id: int

    class Config:
        orm_mode = True
