from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    date: datetime
    kind: OperationKind
    amount: float
    description: Optional[str]

    class Config:
        orm_mode = True