"""
In-memory task storage for the Todo Application.

This module provides CRUD operations for tasks stored in memory.
"""

from typing import Dict, List, Optional
from src.models.task import Task


class TaskStore:
    """
    Manages collection of tasks in memory with CRUD operations.

    Uses dictionary structure with task ID as key for O(1) access.
    """

    def __init__(self):
        """Initialize the task store with empty storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the store with a unique ID.

        Args:
            title: Task title
            description: Optional task description

        Returns:
            The created Task object with assigned ID
        """
        task = Task(id=self._next_id, title=title, description=description, completed=False)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        """
        Update task fields if the task exists.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            completed: New completion status (optional)

        Returns:
            True if update was successful, False otherwise
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the store.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def list_tasks(self, completed_filter: Optional[bool] = None) -> List[Task]:
        """
        List all tasks, optionally filtered by completion status.

        Args:
            completed_filter: If True, return only completed tasks
                            If False, return only pending tasks
                            If None, return all tasks

        Returns:
            List of Task objects matching the filter
        """
        if completed_filter is None:
            return list(self._tasks.values())

        return [task for task in self._tasks.values() if task.completed == completed_filter]

    def get_next_id(self) -> int:
        """
        Get the next available ID (for reference).

        Returns:
            The next available ID
        """
        return self._next_id