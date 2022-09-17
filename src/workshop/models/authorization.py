
import datetime
from typing import Optional
from pydantic import BaseModel, UUID4, Field, validator


# Token base model
class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias='access_token')
    expires: datetime
    token_type: Optional[str] = 'bearer'

    class Config:
        allow_population_by_filed_name = True

    @validator('token')
    def hexlify_token(cls, value):
        return value.hex
