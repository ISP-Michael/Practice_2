from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class TypeUser(Base):
    __tablename__ = 'type_user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type_users: Mapped[str] = mapped_column(String, nullable=False)
