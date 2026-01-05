from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.task import TaskCreate, TaskUpdate, Task
from crud.tasks import (
    get_task as crud_get_task,
    get_tasks as crud_get_tasks,
    create_task as crud_create_task,
    update_task as crud_update_task,
    delete_task as crud_delete_task,
    get_tasks_by_status as crud_get_tasks_by_status
)
from models.task import Task as TaskModel


class TaskService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_task(self, task_id: int) -> Optional[Task]:
        db_task = await crud_get_task(self.db, task_id)
        if db_task is None:
            return None
        return Task.from_orm(db_task)

    async def get_tasks(self, skip: int = 0, limit: int = 100) -> List[Task]:
        db_tasks = await crud_get_tasks(self.db, skip, limit)
        return [Task.from_orm(task) for task in db_tasks]

    async def get_tasks_by_status(self, completed: Optional[bool] = None) -> List[Task]:
        db_tasks = await crud_get_tasks_by_status(self.db, completed)
        return [Task.from_orm(task) for task in db_tasks]

    async def create_task(self, task: TaskCreate) -> Task:
        db_task = await crud_create_task(self.db, task)
        return Task.from_orm(db_task)

    async def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        db_task = await crud_update_task(self.db, task_id, task_update)
        if db_task is None:
            return None
        return Task.from_orm(db_task)

    async def delete_task(self, task_id: int) -> bool:
        return await crud_delete_task(self.db, task_id)