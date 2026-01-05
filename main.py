"""
Main entry point for the Todo Application.

This module orchestrates all components to create a runnable CLI application.
"""

from src.storage.task_store import TaskStore
from src.services.task_service import TaskService
from src.parsers.command_parser import CommandParser
from src.cli.cli_interface import CLIInterface


def main():
    """
    Main function to run the Todo Application.
    """
    # Initialize all components
    task_store = TaskStore()
    task_service = TaskService(task_store)
    command_parser = CommandParser(task_service)
    cli_interface = CLIInterface(task_service, command_parser)

    # Start the application
    cli_interface.run()


if __name__ == "__main__":
    main()