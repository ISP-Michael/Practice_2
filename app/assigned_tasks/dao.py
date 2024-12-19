from app.dao.base import BaseDAO
from app.assigned_tasks.models import AssignedTask, Task, Status


class AssidnedTasksDAO(BaseDAO):
    model = AssignedTask


class TasksDAO(BaseDAO):
    model = Task


class StatusDAO(BaseDAO):
    model = Status
