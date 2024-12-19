from sqlalchemy import String, Integer, TIMESTAMP, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime


class AssignedTask(Base):
    __tablename__ = 'assigned_tasks'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    deadline: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)


class Status(Base):
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)




