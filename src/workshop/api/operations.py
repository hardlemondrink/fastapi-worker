from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation, OperationKind
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=List[Operation])
def get_opertaions(kind: Optional[OperationKind] = None, service: OperationsService = Depends()):
    return service.get_list(kind=kind)


@router.post('/', response_model=Operation)
def create_operation(service: OperationsService = Depends()):
    pass
