from datetime import datetime
import typing
from dashboard.models import Base
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import TIMESTAMP, String


class Task(Base):
    # TODO: implement Task CRUD operations
    __tablename__ = "task"

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(60), nullable=True)
    description: Mapped[typing.Optional[str]] = mapped_column(
        String(200), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

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
