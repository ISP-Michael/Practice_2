from pydantic import BaseModel, Field
from typing import Optional


class UserTypeRead(BaseModel):
    id: int = Field(..., description='Идентификатор пользователя')
    usertype: str = Field(..., min_length=3, max_length=50)


class UserTypeCreate(BaseModel):
    usertype: str = Field(..., min_length=3, max_length=50)


class UserTypeUpdate(BaseModel):
    usertype: str = Field(..., min_length=3, max_length=50)
