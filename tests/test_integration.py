"""
Integration tests for the Todo Application.

Tests that components work together correctly.
"""

from src.storage.task_store import TaskStore
from src.services.task_service import TaskService
from src.parsers.command_parser import CommandParser
from src.cli.cli_interface import CLIInterface


def test_add_and_list_task_integration():
    """Test adding a task and then listing it."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    add_response = parser.parse_and_execute('add "Test Task" "Test Description"')
    assert "Task added with ID: 1" in add_response

    # List all tasks
    list_response = parser.parse_and_execute('list')
    assert "Test Task" in list_response
    assert "Test Description" in list_response
    assert "Pending" in list_response


def test_update_task_integration():
    """Test adding a task and then updating it."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    add_response = parser.parse_and_execute('add "Original Task" "Original Description"')
    assert "Task added with ID: 1" in add_response

    # Update the task
    update_response = parser.parse_and_execute('update 1 "Updated Task" "Updated Description"')
    assert "Task 1 updated successfully" in update_response

    # Verify the update by listing
    list_response = parser.parse_and_execute('list')
    assert "Updated Task" in list_response
    assert "Updated Description" in list_response


def test_complete_task_integration():
    """Test adding a task and then marking it complete."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    add_response = parser.parse_and_execute('add "Test Task"')
    assert "Task added with ID: 1" in add_response

    # Mark as complete
    complete_response = parser.parse_and_execute('complete 1')
    assert "Task 1 marked as complete" in complete_response

    # Verify by listing completed tasks
    list_completed_response = parser.parse_and_execute('list completed')
    assert "Test Task" in list_completed_response
    assert "Complete" in list_completed_response

    # Verify it's not in pending tasks
    list_pending_response = parser.parse_and_execute('list pending')
    assert "Test Task" not in list_pending_response


def test_delete_task_integration():
    """Test adding a task and then deleting it."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    add_response = parser.parse_and_execute('add "Test Task"')
    assert "Task added with ID: 1" in add_response

    # Verify it exists
    list_response = parser.parse_and_execute('list')
    assert "Test Task" in list_response

    # Delete the task
    delete_response = parser.parse_and_execute('delete 1')
    assert "Task 1 deleted successfully" in delete_response

    # Verify it's gone
    list_response_after = parser.parse_and_execute('list')
    assert "Test Task" not in list_response_after


def test_command_error_handling():
    """Test that invalid commands are handled properly."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Test invalid command
    response = parser.parse_and_execute('invalidcommand')
    assert "Unknown command" in response

    # Test command with missing arguments
    response = parser.parse_and_execute('add')
    assert "Error: Missing required arguments" in response

    # Test command with invalid task ID
    response = parser.parse_and_execute('update abc "title"')
    assert "Error: Task ID must be a number" in response


def test_list_filters():
    """Test that list filters work correctly."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add tasks
    parser.parse_and_execute('add "Pending Task"')
    parser.parse_and_execute('add "Completed Task"')

    # Mark one as complete
    parser.parse_and_execute('complete 2')

    # Test list all
    all_response = parser.parse_and_execute('list')
    assert "Pending Task" in all_response
    assert "Completed Task" in all_response

    # Test list pending
    pending_response = parser.parse_and_execute('list pending')
    assert "Pending Task" in pending_response
    assert "Completed Task" not in pending_response

    # Test list completed
    completed_response = parser.parse_and_execute('list completed')
    assert "Completed Task" in completed_response
    assert "Pending Task" not in completed_response