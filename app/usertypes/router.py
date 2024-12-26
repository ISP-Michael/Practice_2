from fastapi import APIRouter, Response, status
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.exceptions import UserAlreadyExistsException, NoUserIdException
from app.usertypes.dao import UserTypesDAO
from app.usertypes.schemas import UserTypeRead, UserTypeCreate, UserTypeUpdate
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix='/utype', tags=['UType'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/', response_class=HTMLResponse, summary='To-Do List')
async def get_todo_list(request: Request):
    return templates.TemplateResponse('crudUserType.html',
                                      {'request': request})



@router.get('/usertypes/{usertype_id}')
async def get_usertype(usertype_id: int):
    usertype = await UserTypesDAO.find_one_or_none_by_id(usertype_id)
    if not usertype:
        raise NoUserIdException
    return UserTypeRead(id=usertype.id, usertype=usertype.usertype)


@router.get('/usertypes')
async def get_usertypes():
    user_types_all = await UserTypesDAO.find_all()
    return user_types_all


@router.post('/addUserType')
async def create_usertype(user_type: UserTypeCreate):
    existing_usertype = await UserTypesDAO.add(usertype=user_type.usertype)
    return existing_usertype


@router.put('/updateUserType/{id}')
async def update_user_type(id: int, user_type: UserTypeUpdate):
    db_user_type = await UserTypesDAO.find_one_or_none_by_id(data_id=id)
    if db_user_type is None:
        raise NoUserIdException
    result = await UserTypesDAO.update(db_user_type, user_type)
    return result


@router.delete('/deleteUserType/{usertype_id}')
async def delete_user_type(usertype_id: int):
    user_type = await UserTypesDAO.delete(usertype_id)
    if not user_type:
        raise NoUserIdException
    return Response(status_code=status.HTTP_204_NO_CONTENT)


