from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from app.database import async_session_maker
from fastapi.encoders import jsonable_encoder


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance

    @classmethod
    async def update(cls, db_obj, obj_in):
        async with async_session_maker() as session:
            async with session.begin():
                obj_data = jsonable_encoder(db_obj)
                if isinstance(obj_in, dict):
                    update_data = obj_in
                else:
                    update_data = obj_in.dict(exclude_unset=True)
                for field in obj_data:
                    if field in update_data:
                        setattr(db_obj, field, update_data[field])
                session.add(db_obj)
                await session.commit()
                return db_obj

    @classmethod
    async def delete(cls, data_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            if result is None:
                return {}
            obj = result.scalar()
            await session.delete(obj)
            await session.commit()
            return obj


