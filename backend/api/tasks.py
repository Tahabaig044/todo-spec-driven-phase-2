from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from database import get_db
from schemas.task import Task, TaskCreate, TaskUpdate
from services.task_service import TaskService

router = APIRouter()


@router.get("/tasks", response_model=List[Task], tags=["tasks"])
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Get all tasks with optional filtering by completion status.
    """
    service = TaskService(db)

    if completed is not None:
        tasks = await service.get_tasks_by_status(completed)
    else:
        tasks = await service.get_tasks(skip, limit)

    return tasks


@router.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get a specific task by ID.
    """
    service = TaskService(db)
    task = await service.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new task.
    """
    service = TaskService(db)
    return await service.create_task(task)


@router.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    """
    Update an existing task.
    """
    service = TaskService(db)
    updated_task = await service.update_task(task_id, task)

    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return updated_task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK, tags=["tasks"])
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a task.
    """
    service = TaskService(db)
    success = await service.delete_task(task_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}