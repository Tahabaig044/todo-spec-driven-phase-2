"""
Unit tests for the Task Service.

Tests all business logic in the Task Service.
"""

import pytest
from src.models.task import Task
from src.storage.task_store import TaskStore
from src.services.task_service import TaskService


def test_add_task():
    """Test adding a task through the service."""
    store = TaskStore()
    service = TaskService(store)

    task = service.add_task("Test task", "Test description")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.completed is False

    tasks = service.list_tasks()
    assert len(tasks) == 1


def test_add_task_validation():
    """Test that adding a task with empty title raises an error."""
    store = TaskStore()
    service = TaskService(store)

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.add_task("")


def test_add_task_title_with_whitespace():
    """Test that adding a task with whitespace-only title raises an error."""
    store = TaskStore()
    service = TaskService(store)

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.add_task("   ")


def test_list_tasks():
    """Test listing tasks through the service."""
    store = TaskStore()
    service = TaskService(store)

    service.add_task("Task 1")
    service.add_task("Task 2")

    tasks = service.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_list_tasks_filtered():
    """Test listing tasks with filters."""
    store = TaskStore()
    service = TaskService(store)

    service.add_task("Pending task")
    completed_task = service.add_task("Completed task")
    service.mark_task_complete(completed_task.id)

    # Test completed filter
    completed_tasks = service.list_tasks(completed_filter=True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0].completed is True

    # Test pending filter
    pending_tasks = service.list_tasks(completed_filter=False)
    assert len(pending_tasks) == 1
    assert pending_tasks[0].completed is False


def test_update_task():
    """Test updating a task through the service."""
    store = TaskStore()
    service = TaskService(store)

    original_task = service.add_task("Original task", "Original description")

    success = service.update_task(original_task.id, "Updated title", "Updated description")

    assert success is True
    updated_task = store.get_task(original_task.id)
    assert updated_task is not None
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Updated description"


def test_update_task_validation():
    """Test that updating a task with empty title raises an error."""
    store = TaskStore()
    service = TaskService(store)

    task = service.add_task("Original task")

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.update_task(task.id, "")


def test_update_nonexistent_task():
    """Test updating a non-existent task returns False."""
    store = TaskStore()
    service = TaskService(store)

    success = service.update_task(999, "New title")
    assert success is False


def test_delete_task():
    """Test deleting a task through the service."""
    store = TaskStore()
    service = TaskService(store)

    task = service.add_task("Test task")

    success = service.delete_task(task.id)

    assert success is True
    assert store.get_task(task.id) is None
    assert len(service.list_tasks()) == 0


def test_delete_nonexistent_task():
    """Test deleting a non-existent task returns False."""
    store = TaskStore()
    service = TaskService(store)

    success = service.delete_task(999)
    assert success is False


def test_mark_task_complete():
    """Test marking a task as complete."""
    store = TaskStore()
    service = TaskService(store)

    task = service.add_task("Test task")
    assert task.completed is False

    success = service.mark_task_complete(task.id)

    assert success is True
    updated_task = store.get_task(task.id)
    assert updated_task is not None
    assert updated_task.completed is True


def test_mark_task_incomplete():
    """Test marking a task as incomplete."""
    store = TaskStore()
    service = TaskService(store)

    task = service.add_task("Test task")
    service.mark_task_complete(task.id)
    assert task.completed is True

    success = service.mark_task_incomplete(task.id)

    assert success is True
    updated_task = store.get_task(task.id)
    assert updated_task is not None
    assert updated_task.completed is False


def test_mark_nonexistent_task():
    """Test marking completion status of a non-existent task returns False."""
    store = TaskStore()
    service = TaskService(store)

    success = service.mark_task_complete(999)
    assert success is False

    success = service.mark_task_incomplete(999)
    assert success is False