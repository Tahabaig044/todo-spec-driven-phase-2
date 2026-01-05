"""
Command parser for the Todo Application.

This module interprets CLI commands and maps them to service operations.
"""

import re
from typing import Dict, List, Optional, Tuple
from src.services.task_service import TaskService


class CommandParser:
    """
    Parses user commands and maps them to appropriate service operations.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the command parser with a task service.

        Args:
            task_service: The service layer to delegate operations to
        """
        self.task_service = task_service

    def parse_and_execute(self, command_line: str) -> str:
        """
        Parse a command line and execute the corresponding operation.

        Args:
            command_line: The command line input from the user

        Returns:
            A string response to display to the user
        """
        command_line = command_line.strip()
        if not command_line:
            return "Please enter a command. Type 'help' for available commands."

        # Split command and arguments, preserving quoted strings
        parts = self._parse_command_line(command_line)
        if not parts:
            return "Invalid command format. Type 'help' for available commands."

        command = parts[0].lower()

        # Map commands to their respective handlers
        command_handlers = {
            'add': self._handle_add,
            'list': self._handle_list,
            'update': self._handle_update,
            'delete': self._handle_delete,
            'complete': self._handle_complete,
            'incomplete': self._handle_incomplete,
            'help': self._handle_help,
            'quit': self._handle_quit,
            'exit': self._handle_quit,
        }

        if command in command_handlers:
            try:
                return command_handlers[command](parts[1:])
            except ValueError as e:
                return f"Error: {str(e)}"
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return f"Unknown command: {command}. Type 'help' for available commands."

    def _parse_command_line(self, command_line: str) -> List[str]:
        """
        Parse a command line into parts, preserving quoted strings.

        Args:
            command_line: The raw command line

        Returns:
            List of command parts
        """
        # This regex finds quoted strings or whitespace-separated words
        pattern = r'"([^"]*)"|\'([^\']*)\'|(\S+)'
        matches = re.findall(pattern, command_line)
        # Each match is a tuple of (double_quoted, single_quoted, unquoted)
        parts = [match[0] or match[1] or match[2] for match in matches]
        return parts

    def _handle_add(self, args: List[str]) -> str:
        """Handle the 'add' command."""
        if len(args) < 1:
            return "Error: Missing required arguments for 'add'. Usage: add \"title\" [\"description\"]"

        title = args[0]
        description = args[1] if len(args) > 1 else None

        try:
            task = self.task_service.add_task(title, description)
            return f"Task added with ID: {task.id}"
        except ValueError as e:
            return f"Error: {str(e)}"

    def _handle_list(self, args: List[str]) -> str:
        """Handle the 'list' command."""
        if len(args) == 0:
            # List all tasks
            tasks = self.task_service.list_tasks()
        elif len(args) == 1 and args[0].lower() == 'completed':
            # List completed tasks only
            tasks = self.task_service.list_tasks(completed_filter=True)
        elif len(args) == 1 and args[0].lower() == 'pending':
            # List pending tasks only
            tasks = self.task_service.list_tasks(completed_filter=False)
        else:
            return "Error: Invalid arguments for 'list'. Usage: list [completed|pending]"

        if not tasks:
            return "No tasks found."

        # Format the task list
        result = "ID  Title                 Description           Status\n"
        result += "--  -----                 -----------           ------\n"
        for task in tasks:
            status = "Complete" if task.completed else "Pending"
            desc = task.description or ""
            # Truncate long titles and descriptions for display
            title_display = task.title[:20] + "..." if len(task.title) > 20 else task.title
            desc_display = desc[:18] + "..." if len(desc) > 18 else desc
            result += f"{task.id:<3} {title_display:<20} {desc_display:<20} {status}\n"

        return result.rstrip()

    def _handle_update(self, args: List[str]) -> str:
        """Handle the 'update' command."""
        if len(args) < 2:
            return "Error: Missing required arguments for 'update'. Usage: update <id> \"new_title\" [\"new_description\"]"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be a number."

        title = args[1]
        description = args[2] if len(args) > 2 else None

        success = self.task_service.update_task(task_id, title, description)
        if success:
            return f"Task {task_id} updated successfully"
        else:
            return f"Error: Task with ID {task_id} does not exist."

    def _handle_delete(self, args: List[str]) -> str:
        """Handle the 'delete' command."""
        if len(args) != 1:
            return "Error: Missing required arguments for 'delete'. Usage: delete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be a number."

        success = self.task_service.delete_task(task_id)
        if success:
            return f"Task {task_id} deleted successfully"
        else:
            return f"Error: Task with ID {task_id} does not exist."

    def _handle_complete(self, args: List[str]) -> str:
        """Handle the 'complete' command."""
        if len(args) != 1:
            return "Error: Missing required arguments for 'complete'. Usage: complete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be a number."

        success = self.task_service.mark_task_complete(task_id)
        if success:
            return f"Task {task_id} marked as complete"
        else:
            return f"Error: Task with ID {task_id} does not exist."

    def _handle_incomplete(self, args: List[str]) -> str:
        """Handle the 'incomplete' command."""
        if len(args) != 1:
            return "Error: Missing required arguments for 'incomplete'. Usage: incomplete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be a number."

        success = self.task_service.mark_task_incomplete(task_id)
        if success:
            return f"Task {task_id} marked as incomplete"
        else:
            return f"Error: Task with ID {task_id} does not exist."

    def _handle_help(self, args: List[str]) -> str:
        """Handle the 'help' command."""
        help_text = """
Available commands:
  add "title" ["description"]    - Add a new task
  list                          - List all tasks
  list completed                - List completed tasks only
  list pending                  - List pending tasks only
  update <id> "new_title" ["new_description"] - Update a task
  complete <id>                 - Mark task as complete
  incomplete <id>               - Mark task as incomplete
  delete <id>                   - Delete a task
  help                          - Show available commands
  quit/exit                     - Exit the application
        """.strip()
        return help_text

    def _handle_quit(self, args: List[str]) -> str:
        """Handle the 'quit' command."""
        return "quit"