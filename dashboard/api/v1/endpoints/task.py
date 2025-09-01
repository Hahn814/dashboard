from fastapi import Request
from dashboard.api.v1 import router
from dashboard.models.task import Task
from sqlalchemy.orm import Session


@router.get("/tasks/{task_id}")
def get_task(task_id: int, request: Request):
    task = None
    with Session(request.app.state.db.engine) as session:
        task = Task.get_task(task_id, session)

    return task


@router.get("/tasks/")
def get_tasks(request: Request):
    with Session(request.app.state.db.engine) as session:
        tasks = Task.get_tasks(session)

    return tasks
