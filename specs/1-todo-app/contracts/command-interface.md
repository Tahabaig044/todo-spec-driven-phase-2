# Todo Application Command Interface Specification

## Command Format
The application accepts commands in the following format:
```
command [arguments...]
```

## Available Commands

### Add Task
- **Command**: `add`
- **Arguments**: `"title"` `["description"]`
- **Description**: Creates a new task with the specified title and optional description
- **Success Response**: "Task added with ID: {id}"
- **Error Response**: "Error: {error_message}"
- **Example**: `add "Buy groceries" "Milk, bread, eggs"`

### List Tasks
- **Command**: `list`
- **Arguments**: `["completed" | "pending"]`
- **Description**: Lists all tasks or filters by completion status
- **Success Response**: Formatted list of tasks
- **Error Response**: "Error: {error_message}"
- **Examples**:
  - `list` - Lists all tasks
  - `list completed` - Lists only completed tasks
  - `list pending` - Lists only pending tasks

### Update Task
- **Command**: `update`
- **Arguments**: `<id>` `"new_title"` `["new_description"]`
- **Description**: Updates the title and/or description of an existing task
- **Success Response**: "Task {id} updated successfully"
- **Error Response**: "Error: {error_message}"
- **Example**: `update 1 "Updated title" "Updated description"`

### Complete Task
- **Command**: `complete`
- **Arguments**: `<id>`
- **Description**: Marks a task as completed
- **Success Response**: "Task {id} marked as complete"
- **Error Response**: "Error: {error_message}"
- **Example**: `complete 1`

### Incomplete Task
- **Command**: `incomplete`
- **Arguments**: `<id>`
- **Description**: Marks a completed task as incomplete
- **Success Response**: "Task {id} marked as incomplete"
- **Error Response**: "Error: {error_message}"
- **Example**: `incomplete 1`

### Delete Task
- **Command**: `delete`
- **Arguments**: `<id>`
- **Description**: Removes a task from the system
- **Success Response**: "Task {id} deleted successfully"
- **Error Response**: "Error: {error_message}"
- **Example**: `delete 1`

### Help
- **Command**: `help`
- **Arguments**: None
- **Description**: Displays available commands and their usage
- **Success Response**: Help text with command descriptions
- **Example**: `help`

### Quit
- **Command**: `quit`
- **Arguments**: None
- **Description**: Exits the application
- **Success Response**: Application terminates
- **Example**: `quit`

## Error Handling
- Invalid command: "Unknown command: {command}. Type 'help' for available commands."
- Missing arguments: "Error: Missing required arguments for '{command}'."
- Invalid task ID: "Error: Task with ID {id} does not exist."
- Invalid argument format: "Error: Invalid argument format for '{command}'."
- Empty title: "Error: Task title cannot be empty."

## Response Format
All responses follow the format:
- Success: Plain text confirmation message
- Error: "Error: {descriptive message}"
- List output: Formatted table with columns: ID, Title, Description, Status