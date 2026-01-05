"""
CLI interface for the Todo Application.

This module manages user interaction loop and formatted output display.
"""

from src.services.task_service import TaskService
from src.parsers.command_parser import CommandParser


class CLIInterface:
    """
    Manages user interaction loop and formatted output display.
    """

    def __init__(self, task_service: TaskService, command_parser: CommandParser):
        """
        Initialize the CLI interface with required services.

        Args:
            task_service: The service layer for task operations
            command_parser: The parser for command interpretation
        """
        self.task_service = task_service
        self.command_parser = command_parser
        self.running = True

    def run(self):
        """
        Start the main application loop.
        """
        print("Welcome to the Todo Application!")
        print("Type 'help' for available commands.")

        while self.running:
            try:
                command = input("\n> ").strip()
                if not command:
                    continue

                response = self.command_parser.parse_and_execute(command)

                if response == "quit":
                    self.running = False
                    print("Goodbye!")
                else:
                    print(response)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break