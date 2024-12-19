from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix='/assigned_tasks', tags=['Assigned Tasks'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/', response_class=HTMLResponse, summary='To-Do List')
async def get_todo_list(request: Request):
    return templates.TemplateResponse('assigned_tasks.html',
                                      {'request': request})



