from app.dao.base import BaseDAO
from app.usertypes.models import UserType


class UserTypesDAO(BaseDAO):
    model = UserType
