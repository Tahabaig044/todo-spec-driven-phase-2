"""
Unit tests for the Task model.

Tests all functionality and validation in the Task model.
"""

import pytest
from src.models.task import Task


def test_task_creation():
    """Test creating a valid task."""
    task = Task(id=1, title="Test task", description="Test description", completed=False)
    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.completed is False


def test_task_creation_defaults():
    """Test creating a task with default values."""
    task = Task(id=1, title="Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.description is None
    assert task.completed is False


def test_task_title_validation():
    """Test that task title cannot be empty."""
    with pytest.raises(ValueError, match="Task title is required and cannot be empty"):
        Task(id=1, title="")


def test_task_title_with_whitespace_only():
    """Test that task title with only whitespace is invalid."""
    with pytest.raises(ValueError, match="Task title is required and cannot be empty"):
        Task(id=1, title="   ")


def test_task_title_with_whitespace():
    """Test that task title with content and whitespace is valid."""
    task = Task(id=1, title="   Valid Title   ")
    assert task.title == "   Valid Title   "


def test_task_id_validation():
    """Test that task ID must be a non-negative integer."""
    with pytest.raises(ValueError, match="Task ID must be a non-negative integer"):
        Task(id=-1, title="Test task")


def test_task_id_zero():
    """Test that task ID can be zero."""
    task = Task(id=0, title="Test task")
    assert task.id == 0


def test_task_completed_validation():
    """Test that completed status must be a boolean."""
    with pytest.raises(ValueError, match="Completed status must be a boolean"):
        Task(id=1, title="Test task", completed="not_a_boolean")


def test_task_completed_true():
    """Test that completed status can be True."""
    task = Task(id=1, title="Test task", completed=True)
    assert task.completed is True


def test_task_completed_false():
    """Test that completed status can be False."""
    task = Task(id=1, title="Test task", completed=False)
    assert task.completed is False