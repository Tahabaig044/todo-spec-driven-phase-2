# Todo Application Quickstart Guide

## Prerequisites
- Python 3.13+ installed on your system

## Running the Application

1. Navigate to the project directory
2. Execute the main application file:
   ```bash
   python main.py
   ```

## Getting Started

When you first run the application, you'll see a welcome message and a prompt waiting for commands:

```
Welcome to the Todo Application!
Type 'help' for available commands.
>
```

## Basic Operations

### Adding a Task
To add a new task, use the `add` command followed by the title in quotes:
```
> add "Buy groceries"
Task added with ID: 1
```

You can also add a description:
```
> add "Buy groceries" "Milk, bread, and eggs"
Task added with ID: 2
```

### Viewing Tasks
To see all your tasks, use the `list` command:
```
> list
ID  Title             Description          Status
--  -----             -----------          ------
1   Buy groceries                          Pending
2   Buy groceries     Milk, bread, and eggs Pending
```

To see only completed tasks:
```
> list completed
ID  Title    Description    Status
--  -----    -----------    ------
```

To see only pending tasks:
```
> list pending
ID  Title             Description          Status
--  -----             -----------          ------
1   Buy groceries                          Pending
2   Buy groceries     Milk, bread, and eggs Pending
```

### Updating a Task
To update a task, use the `update` command with the task ID and new details:
```
> update 1 "Buy weekly groceries" "Milk, bread, eggs, fruits, and vegetables"
Task 1 updated successfully
```

### Marking a Task Complete
To mark a task as complete, use the `complete` command:
```
> complete 1
Task 1 marked as complete
```

### Marking a Task Incomplete
To mark a completed task as incomplete again, use the `incomplete` command:
```
> incomplete 1
Task 1 marked as incomplete
```

### Deleting a Task
To delete a task, use the `delete` command:
```
> delete 1
Task 1 deleted successfully
```

### Getting Help
To see all available commands, use the `help` command:
```
> help
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
  quit                          - Exit the application
```

### Exiting the Application
To exit the application, use the `quit` command:
```
> quit
Goodbye!
```

## Example Workflow

Here's a complete example of using the application:

```
Welcome to the Todo Application!
Type 'help' for available commands.
> add "Complete project proposal" "Finish the project proposal document"
Task added with ID: 1
> add "Buy groceries"
Task added with ID: 2
> list
ID  Title                    Description                    Status
--  -----                    -----------                    ------
1   Complete project proposal  Finish the project proposal document  Pending
2   Buy groceries                                         Pending
> complete 1
Task 1 marked as complete
> list
ID  Title                    Description                    Status
--  -----                    -----------                    ------
1   Complete project proposal  Finish the project proposal document  Complete
2   Buy groceries                                         Pending
> list completed
ID  Title                    Description                    Status
--  -----                    -----------                    ------
1   Complete project proposal  Finish the project proposal document  Complete
> quit
Goodbye!
```

## Error Handling

The application provides helpful error messages when something goes wrong:

- **Invalid command**: "Unknown command: invalid_cmd. Type 'help' for available commands."
- **Missing arguments**: "Error: Missing required arguments for 'add'."
- **Invalid task ID**: "Error: Task with ID 999 does not exist."
- **Empty title**: "Error: Task title cannot be empty."