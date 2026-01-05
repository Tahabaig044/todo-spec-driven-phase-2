"""
Task service layer for the Todo Application.

This module contains business logic and validation for task operations.
"""

from typing import List, Optional
from src.models.task import Task
from src.storage.task_store import TaskStore


class TaskService:
    """
    Service layer that implements business logic for task operations.
    """

    def __init__(self, task_store: TaskStore):
        """
        Initialize the task service with a task store.

        Args:
            task_store: The storage layer to use for task operations
        """
        self.task_store = task_store

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with validation.

        Args:
            title: Task title (required)
            description: Optional task description

        Returns:
            The created Task object

        Raises:
            ValueError: If title is empty or invalid
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        return self.task_store.add_task(title, description)

    def list_tasks(self, completed_filter: Optional[bool] = None) -> List[Task]:
        """
        List tasks with optional filtering.

        Args:
            completed_filter: If True, return only completed tasks
                            If False, return only pending tasks
                            If None, return all tasks

        Returns:
            List of Task objects matching the filter
        """
        return self.task_store.list_tasks(completed_filter)

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> bool:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if update was successful, False otherwise
        """
        # Validate that the task exists
        existing_task = self.task_store.get_task(task_id)
        if existing_task is None:
            return False

        # Validate title if provided
        if title is not None and (not title or not title.strip()):
            raise ValueError("Task title cannot be empty")

        return self.task_store.update_task(task_id, title, description)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        # Validate that the task exists
        existing_task = self.task_store.get_task(task_id)
        if existing_task is None:
            return False

        return self.task_store.delete_task(task_id)

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if operation was successful, False otherwise
        """
        # Validate that the task exists
        existing_task = self.task_store.get_task(task_id)
        if existing_task is None:
            return False

        return self.task_store.update_task(task_id, completed=True)

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if operation was successful, False otherwise
        """
        # Validate that the task exists
        existing_task = self.task_store.get_task(task_id)
        if existing_task is None:
            return False

        return self.task_store.update_task(task_id, completed=False)