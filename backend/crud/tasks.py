from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from models.task import Task as TaskModel
from schemas.task import TaskCreate, TaskUpdate
from typing import List, Optional


async def get_task(db: AsyncSession, task_id: int) -> Optional[TaskModel]:
    result = await db.execute(select(TaskModel).filter(TaskModel.id == task_id))
    return result.scalar_one_or_none()


async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[TaskModel]:
    result = await db.execute(select(TaskModel).offset(skip).limit(limit))
    return result.scalars().all()


async def create_task(db: AsyncSession, task: TaskCreate) -> TaskModel:
    db_task = TaskModel(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def update_task(db: AsyncSession, task_id: int, task_update: TaskUpdate) -> Optional[TaskModel]:
    # Get the existing task
    existing_task = await get_task(db, task_id)
    if not existing_task:
        return None

    # Prepare update data
    update_data = task_update.model_dump(exclude_unset=True)

    # Update the task
    await db.execute(
        update(TaskModel)
        .where(TaskModel.id == task_id)
        .values(**update_data)
    )
    await db.commit()

    # Refresh and return the updated task
    await db.refresh(existing_task)
    return existing_task


async def delete_task(db: AsyncSession, task_id: int) -> bool:
    result = await db.execute(
        delete(TaskModel)
        .where(TaskModel.id == task_id)
    )
    await db.commit()
    return result.rowcount > 0


async def get_tasks_by_status(db: AsyncSession, completed: Optional[bool] = None) -> List[TaskModel]:
    query = select(TaskModel)
    if completed is not None:
        query = query.where(TaskModel.completed == completed)

    result = await db.execute(query)
    return result.scalars().all()