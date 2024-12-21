from app.dao.base import BaseDAO
from app.assigned_tasks.models import AssignedTask, Task, Status


class AssignedTasksDAO(BaseDAO):
    model = AssignedTask
