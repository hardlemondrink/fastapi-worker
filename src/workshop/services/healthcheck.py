from fastapi import HTTPException, status


class HealthCheckService:
    def healthcheck(self,
                    user_id: int):
        response = HTTPException(status_code=status.HTTP_200_OK)
        return response