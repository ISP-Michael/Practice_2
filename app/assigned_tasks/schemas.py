from pydantic import BaseModel, Field
from datetime import datetime


class AssignedTaskRead(BaseModel):
    id: int = Field(..., description='Дефолтный идентификатор')
    user_id: int = Field(..., description='Идентификатор пользователя')
    task_id: int = Field(..., description='Идентификатор задачи')
    status_id: int = Field(..., description='Идентификатор статуса задачи')
    deadline: datetime = Field(..., description='Время, к которому задача должна быть выполнена')


class AssignedTaskCreate(BaseModel):
    user_id: int = Field(..., description='Идентификатор пользователя')
    task_id: int = Field(..., description='Идентификатор задачи')
    status_id: int = Field(..., description='Идентификатор статуса задачи')
    deadline: datetime = Field(..., description='Время, к которому задача должна быть выполнена')


class AssignedTaskUpdate(BaseModel):
    user_id: int = Field(..., description='Идентификатор пользователя')
    task_id: int = Field(..., description='Идентификатор задачи')
    status_id: int = Field(..., description='Идентификатор статуса задачи')
    deadline: datetime = Field(..., description='Время, к которому задача должна быть выполнена')
