"""
User acceptance tests for the Todo Application.

Tests that verify the application meets user scenario requirements.
"""

from src.storage.task_store import TaskStore
from src.services.task_service import TaskService
from src.parsers.command_parser import CommandParser


def test_scenario_add_new_task():
    """Test Scenario 2: Adding a New Task."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # User adds a task
    response = parser.parse_and_execute('add "Buy groceries" "Milk, bread, eggs"')

    # System assigns an ID and marks the task as incomplete
    assert "Task added with ID:" in response
    assert "1" in response  # Should be ID 1 for first task

    # Task is displayed in the task list
    list_response = parser.parse_and_execute('list')
    assert "Buy groceries" in list_response
    assert "Milk, bread, eggs" in list_response
    assert "Pending" in list_response


def test_scenario_view_tasks():
    """Test Scenario 3: Viewing Tasks."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add some tasks
    parser.parse_and_execute('add "Task 1" "Description 1"')
    parser.parse_and_execute('add "Task 2" "Description 2"')

    # User selects "View Tasks" option
    response = parser.parse_and_execute('list')

    # System displays all tasks with their status
    assert "Task 1" in response
    assert "Task 2" in response
    assert "Description 1" in response
    assert "Description 2" in response
    assert "Pending" in response

    # User can see completed and incomplete tasks separately
    parser.parse_and_execute('complete 1')

    completed_response = parser.parse_and_execute('list completed')
    pending_response = parser.parse_and_execute('list pending')

    assert "Task 1" in completed_response
    assert "Task 2" in pending_response
    assert "Task 1" not in pending_response
    assert "Task 2" not in completed_response


def test_scenario_update_task():
    """Test Scenario 4: Updating a Task."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    parser.parse_and_execute('add "Original Task" "Original Description"')

    # User specifies the task ID to update
    response = parser.parse_and_execute('update 1 "Updated Task" "Updated Description"')

    # User can modify the title, description, or completion status
    assert "Task 1 updated successfully" in response

    # System confirms the update
    list_response = parser.parse_and_execute('list')
    assert "Updated Task" in list_response
    assert "Updated Description" in list_response


def test_scenario_delete_task():
    """Test Scenario 5: Deleting a Task."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    parser.parse_and_execute('add "Task to delete"')

    # User specifies the task ID to delete
    response = parser.parse_and_execute('delete 1')

    # System confirms deletion and removes the task
    assert "Task 1 deleted successfully" in response

    # Task no longer appears in the list
    list_response = parser.parse_and_execute('list')
    assert "Task to delete" not in list_response


def test_scenario_mark_task_complete():
    """Test Scenario 6: Marking Task Complete."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Add a task
    parser.parse_and_execute('add "Incomplete Task"')

    # User specifies the task ID
    response = parser.parse_and_execute('complete 1')

    # System updates the task status to completed
    assert "Task 1 marked as complete" in response

    # Task appears in completed section
    completed_response = parser.parse_and_execute('list completed')
    assert "Incomplete Task" in completed_response
    assert "Complete" in completed_response


def test_cli_interaction_flow():
    """Test Scenario 1: CLI Interaction Flow."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Test help command
    help_response = parser.parse_and_execute('help')
    assert "Available commands:" in help_response
    assert "add" in help_response
    assert "list" in help_response
    assert "update" in help_response
    assert "delete" in help_response
    assert "complete" in help_response
    assert "incomplete" in help_response
    assert "help" in help_response
    assert "quit" in help_response

    # Test multiple operations in sequence
    # Add task
    add_response = parser.parse_and_execute('add "Test Task" "Test Description"')
    assert "Task added with ID:" in add_response

    # List tasks
    list_response = parser.parse_and_execute('list')
    assert "Test Task" in list_response

    # Update task
    update_response = parser.parse_and_execute('update 1 "Updated Task"')
    assert "Task 1 updated successfully" in update_response

    # Mark complete
    complete_response = parser.parse_and_execute('complete 1')
    assert "Task 1 marked as complete" in complete_response

    # Verify final state
    final_list = parser.parse_and_execute('list')
    assert "Updated Task" in final_list
    assert "Complete" in final_list


def test_error_handling_scenarios():
    """Test error handling scenarios."""
    store = TaskStore()
    service = TaskService(store)
    parser = CommandParser(service)

    # Test invalid command
    invalid_response = parser.parse_and_execute('invalidcommand')
    assert "Unknown command:" in invalid_response
    assert "help" in invalid_response

    # Test invalid task ID
    error_response = parser.parse_and_execute('update 999 "title"')
    assert "Task with ID 999 does not exist" in error_response

    # Test missing arguments
    missing_arg_response = parser.parse_and_execute('add')
    assert "Missing required arguments" in missing_arg_response

    # Test empty title
    empty_title_response = parser.parse_and_execute('add ""')
    assert "Task title cannot be empty" in empty_title_response