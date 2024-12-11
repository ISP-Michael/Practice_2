from fastapi import APIRouter, Response
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException, PasswordMismatchException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserAuth


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register/')
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExistsException
    if user_data.password != user_data.password_check:
        raise PasswordMismatchException('Пароли не совпадают')
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name,
                       email=user_data.email,
                       hashed_password=hashed_password)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post('/login/')
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(emamil=user_data.emai, password=user_data.password)
    if check is None:
        raise IncorrectEmailOrPasswordException
    access_token= create_access_token({'sub': str(check.id)})
    response.set_cookie(key='users_access_token', value=access_token, httponly=True)
    return {'ok': True,
            'access_token': access_token,
            'refresh_token': None,
            'message': 'Авторизация успешна!'}


@router.post('/logout/')
async def logout_user(response: Response):
    response.delete_cookie(key='users_access_token')
    return {'message': 'Пользователь успешно вышел из системы'}