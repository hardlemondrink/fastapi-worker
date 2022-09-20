from fastapi import APIRouter, Depends

from ..models.auth import User
from ..services.auth import get_current_user
from ..services.healthcheck import HealthCheckService

router = APIRouter(
    prefix='/healthcheck',
)


@router.get('/')
def healthcheck(service: HealthCheckService = Depends(),
                user: User = Depends(get_current_user)):
    return service.healthcheck(user_id=user.id)