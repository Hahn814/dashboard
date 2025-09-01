import typing
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Task(Base):
    # TODO: implement Task CRUD operations
    __tablename__ = "task"

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<Task(pk={self.pk}, name={self.name})>"

    def __hash__(self):
        return hash((self.pk, self.name))

    @classmethod
    def get_task(cls, task_id: int, db_session: Session) -> typing.Optional["Task"]:
        return db_session.query(cls).filter(cls.pk == task_id).first()

    @classmethod
    def get_tasks(cls, db_session: Session) -> typing.List["Task"]:
        # TODO: Configuration pagination
        return db_session.query(cls).all()
