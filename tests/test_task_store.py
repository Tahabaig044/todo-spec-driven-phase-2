"""
Unit tests for the Task Store.

Tests all CRUD operations in the Task Store.
"""

import pytest
from src.models.task import Task
from src.storage.task_store import TaskStore


def test_task_store_initialization():
    """Test that TaskStore initializes with empty storage."""
    store = TaskStore()
    assert len(store.list_tasks()) == 0
    assert store.get_next_id() == 1


def test_add_task():
    """Test adding a task to the store."""
    store = TaskStore()
    task = store.add_task("Test task", "Test description")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.completed is False

    tasks = store.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1


def test_add_task_auto_id():
    """Test that IDs are assigned sequentially."""
    store = TaskStore()
    task1 = store.add_task("First task")
    task2 = store.add_task("Second task")

    assert task1.id == 1
    assert task2.id == 2
    assert store.get_next_id() == 3


def test_get_task():
    """Test retrieving a task by ID."""
    store = TaskStore()
    added_task = store.add_task("Test task")

    retrieved_task = store.get_task(added_task.id)
    assert retrieved_task is not None
    assert retrieved_task.id == added_task.id
    assert retrieved_task.title == added_task.title


def test_get_nonexistent_task():
    """Test retrieving a non-existent task returns None."""
    store = TaskStore()
    task = store.get_task(999)
    assert task is None


def test_update_task():
    """Test updating a task's properties."""
    store = TaskStore()
    original_task = store.add_task("Original task", "Original description")

    success = store.update_task(original_task.id, "Updated title", "Updated description", True)

    assert success is True
    updated_task = store.get_task(original_task.id)
    assert updated_task is not None
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Updated description"
    assert updated_task.completed is True


def test_update_nonexistent_task():
    """Test updating a non-existent task returns False."""
    store = TaskStore()
    success = store.update_task(999, "New title")
    assert success is False


def test_update_task_partial():
    """Test updating only specific fields of a task."""
    store = TaskStore()
    original_task = store.add_task("Original task", "Original description")

    # Update only the title
    success = store.update_task(original_task.id, title="Updated title")

    assert success is True
    updated_task = store.get_task(original_task.id)
    assert updated_task is not None
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Original description"  # Should remain unchanged
    assert updated_task.completed is False  # Should remain unchanged


def test_delete_task():
    """Test deleting a task."""
    store = TaskStore()
    task = store.add_task("Test task")

    success = store.delete_task(task.id)

    assert success is True
    assert store.get_task(task.id) is None
    assert len(store.list_tasks()) == 0


def test_delete_nonexistent_task():
    """Test deleting a non-existent task returns False."""
    store = TaskStore()
    success = store.delete_task(999)
    assert success is False


def test_list_tasks():
    """Test listing all tasks."""
    store = TaskStore()
    task1 = store.add_task("Task 1")
    task2 = store.add_task("Task 2")

    tasks = store.list_tasks()
    assert len(tasks) == 2
    assert {task.id for task in tasks} == {1, 2}


def test_list_tasks_filtered_completed():
    """Test listing tasks filtered by completed status."""
    store = TaskStore()
    pending_task = store.add_task("Pending task")
    completed_task = store.add_task("Completed task")
    store.update_task(completed_task.id, completed=True)

    completed_tasks = store.list_tasks(completed_filter=True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0].id == 2
    assert completed_tasks[0].completed is True


def test_list_tasks_filtered_pending():
    """Test listing tasks filtered by pending status."""
    store = TaskStore()
    pending_task = store.add_task("Pending task")
    completed_task = store.add_task("Completed task")
    store.update_task(completed_task.id, completed=True)

    pending_tasks = store.list_tasks(completed_filter=False)
    assert len(pending_tasks) == 1
    assert pending_tasks[0].id == 1
    assert pending_tasks[0].completed is False


def test_list_tasks_unfiltered():
    """Test listing all tasks without filter."""
    store = TaskStore()
    pending_task = store.add_task("Pending task")
    completed_task = store.add_task("Completed task")
    store.update_task(completed_task.id, completed=True)

    all_tasks = store.list_tasks(completed_filter=None)
    assert len(all_tasks) == 2
    task_ids = {task.id for task in all_tasks}
    assert task_ids == {1, 2}