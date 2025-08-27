# TODO: Implement Task model
# TODO: Implement CRUD operations

from dashboard.api.v1 import router
from dashboard.core.mock import TASK_MOCK_TABLE

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((item for item in TASK_MOCK_TABLE if item["task_id"] == task_id), None)
    return task

@router.get("/tasks/")
def get_tasks():
    return TASK_MOCK_TABLE