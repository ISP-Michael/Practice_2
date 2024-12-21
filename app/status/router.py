from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.status.schemas import StatusCreate, StatusUpdate, StatusRead
from app.status.dao import StatusDAO


router = APIRouter(prefix='/status', tags=['Status'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/Status/{id}')
async def get_status(id: int, status: StatusCreate):
    current_status = await StatusDAO.find_one_or_none_by_id(data_id=id)
    if current_status is None:
        raise Exception('Статус не найден. Получено значение None')
    return current_status


@router.post('/addStatus')
async def create_status(status: StatusCreate):
    await StatusDAO.add(title=status.title)


@router.put('/updateStatus/{id}')
async def update_task(id: int, status: StatusUpdate):
    current_status = await StatusDAO.find_one_or_none_by_id(data_id=id)
    if current_status is None:
        raise Exception('Статус не найден. Получено значение None')
    await StatusDAO.update(current_status, status)


@router.delete('/deleteTask/{id}')
async def delete_task(id: int):
    status_to_delete = await StatusDAO.find_one_or_none_by_id(data_id=id)
    if status_task is None:
        raise Exception('Статус (который нужно удалить) не найден. Получено значение None')
    await StatusDAO.delete(status_to_delete)

