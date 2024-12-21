from pydantic import BaseModel, Field


class StatusRead(BaseModel):
    id: int = Field(..., description='Идентификатор пользователя')
    title: str = Field(..., min_length=3, max_length=50)


class StatusCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)


class StatusUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
