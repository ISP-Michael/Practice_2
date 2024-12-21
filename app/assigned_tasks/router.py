from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.assigned_tasks.schemas import AssignedTaskCreate, AssignedTaskUpdate, AssignedTaskRead
from app.assigned_tasks.dao import AssignedTasksDAO


router = APIRouter(prefix='/assigned_tasks', tags=['Assigned Tasks'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/', response_class=HTMLResponse, summary='To-Do List')
async def get_todo_list(request: Request):
    return templates.TemplateResponse('assigned_tasks.html',
                                      {'request': request})


@router.post('/addAssignedTask')
async def add_assigned_task(assigned_task: AssignedTaskCreate):
    pass


