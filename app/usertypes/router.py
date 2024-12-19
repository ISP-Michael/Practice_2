from fastapi import APIRouter, Response, status
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.exceptions import UserAlreadyExistsException, NoUserIdException
from app.usertypes.dao import UserTypesDAO
from app.usertypes.schemas import UserTypeRead, UserTypeCreate, UserTypeUpdate


router = APIRouter(prefix='/utype', tags=['UType'])


@router.get('/usertypes/{usertype_id}')
async def get_usertype(usertype_id: int):
    usertype = await UserTypesDAO.find_one_of_none_by_id(usertype_id)
    if not usertype:
        raise NoUserIdException
    return UserTypeRead(id=usertype.id, usertype=usertype.usertype)


@router.get('/usertypes')
async def get_usertypes():
    user_types_all = await UserTypesDAO.find_all()
    return user_types_all


@router.post('/addUserType')
async def create_usertype(user_type: UserTypeCreate):
    existing_usertype = await UserTypesDAO.find_one_or_none(usertype=user_type.usertype)
    if existing_usertype:
        raise UserTypeAlreadyExistsException
    await UserTypesDAO.add(usertype=user_type.usertype)
    return {'message': 'ok'}


@router.put('/updateUserType/{id}')
async def update_user_type(id: int, user_type: UserTypeUpdate):
    db_user_type = await UserTypesDAO.find_one_or_none_by_id(data_id=id)
    if not db_user_type:
        raise NoUserIdException
    await UserTypesDAO.update(db_user_type, user_type)
    return {'message': 'ok'}


@router.delete('/deleteUserType/{usertype_id}')
async def delete_user_type(usertype_id: int):
    user_type = await UserTypesDAO.delete(usertype_id)
    if not user_type:
        raise NoUserIdException
    return Response(status_code=status.HTTP_204_NO_CONTENT)

