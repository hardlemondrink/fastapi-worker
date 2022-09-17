from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr

from ..models.authorization import TokenBase


class RegistrationKind(str, Enum):
    VK_ID = 'vk_id'
    YA_ID = 'yandex_id'
    APPLE_ID = 'apple_id'
    GOOGLE_ID = 'google_id'
    EMAIL = 'email'
    PHONE = 'phone'


# Base model
class UserBase(BaseModel):
    id: int
    isActive: bool

    class Config:
        orm_mode = True
        

# Default model
class User(UserBase):
    login: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    phoneNumber: Optional[str]           # localized  format 79991112233
    country: Optional[str]
    registration_type : RegistrationKind # VK ID / Yandex ID / Apple ID / E-Mail / Phone / Google ID
    registration_date = datetime
    registration_data = str              # authorization data from ID's (YA ID / Google ID/ Apple ID)  
    token: TokenBase = {} 


# Create user when registration is success
class UserCreate(UserBase):
    pass


# Update user data when logged
class UserUpdate(UserBase):
    pass