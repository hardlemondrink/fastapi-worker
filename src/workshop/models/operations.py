from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    date: datetime
    kind: OperationKind
    amount: float
    description: Optional[str]


class Operation(OperationBase):
    id: int
    isActive: bool

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase):
    pass
