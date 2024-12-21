from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.tasks.schemas import TaskCreate, TaskUpdate, TaskRead
from app.tasks.dao import TasksDAO


router = APIRouter(prefix='/tasks', tags=['Tasks'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/Task/{id}')
async def get_task(id: int, task: TaskCreate):
    current_task = await TasksDAO.find_one_or_none_by_id(data_id=id)
    if current_task is None:
        raise Exception('Задача не найдена. Получено значение None')
    return current_task


@router.post('/addTask')
async def create_task(task: TaskCreate):
    await TasksDAO.add(title=task.title, description=task.description)


@router.put('/updateTask/{id}')
async def update_task(id: int, task: TaskUpdate):
    current_task = await TasksDAO.find_one_or_none_by_id(data_id=id)
    if current_task is None:
        raise Exception('Задача не найдена. Получено значение None')
    await TasksDAO.update(current_task, task)


@router.delete('/deleteTask/{id}')
async def delete_task(id: int):
    task_to_delete = await TasksDAO.find_one_or_none_by_id(data_id=id)
    if current_task is None:
        raise Exception('Задача (которую нужно удалить) не найдена. Получено значение None')
    await TasksDAO.delete(task_to_delete)

