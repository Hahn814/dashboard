import typing
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "task"

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<Task(pk={self.pk}, name={self.name})>"
