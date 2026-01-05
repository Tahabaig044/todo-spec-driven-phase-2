"""
Task model for the Todo Application.

This module defines the Task data model with validation according to specification requirements.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Task title that describes what needs to be done
        description (Optional[str]): Additional details about the task
        completed (bool): Indicates whether the task has been completed
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title is required and cannot be empty")
        if not isinstance(self.id, int) or self.id < 0:
            raise ValueError("Task ID must be a non-negative integer")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed status must be a boolean")