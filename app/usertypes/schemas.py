from pydantic import BaseModel, Field


class UserTypeRead(BaseModel):
    id: int = Field(..., description='Идентификатор пользователя')
    usertype: str = Field(..., min_length=3, max_length=50)

    class Config:
        from_attributes = True


class UserTypeCreate(BaseModel):
    usertype: str = Field(..., min_length=3, max_length=50)


class UserTypeUpdate(BaseModel):
    usertype: str = Field(..., min_length=3, max_length=50)
