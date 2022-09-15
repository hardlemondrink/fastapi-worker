from typing import List, Optional
from webbrowser import Opera
from xmlrpc.client import Boolean

from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation, OperationCreate, OperationKind
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=List[Operation])
def get_opertaions(kind: Optional[OperationKind] = None, service: OperationsService = Depends()):
    return service.get_list(kind=kind)


@router.post('/', response_model=Operation)
def create_operation(operation_data: OperationCreate, service: OperationsService = Depends()):
    return service.create(operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(operation_id: int, service: OperationsService = Depends()):
    return service.get(operation_id=operation_id)


@router.delete('/', response_model=Boolean)
def delete_operation(operation_id: int, service: OperationsService = Depends()):
    return service.delete(operation_id=operation_id)