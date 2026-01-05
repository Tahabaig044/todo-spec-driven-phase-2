# Todo Application Technical Plan - Phase 1

## High-Level Architecture

The Todo Application follows a clean architecture pattern with clear separation of concerns:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CLI Layer     │    │  Service Layer   │    │  Data Layer     │
│                 │    │                  │    │                 │
│ - Command       │    │ - Business Logic │    │ - In-Memory     │
│   Processing    │───▶│ - Validation     │───▶│   Task Storage  │
│ - User          │    │ - Operations     │    │ - Task Model    │
│   Interaction   │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Layer Responsibilities:
- **CLI Layer**: Handles user input/output, command parsing, and display formatting
- **Service Layer**: Contains business logic, validation, and operation orchestration
- **Data Layer**: Manages task data structure and in-memory storage

## Core Components and Their Responsibilities

### 1. Task Model
- **Responsibility**: Defines the structure and validation rules for task entities
- **Fields**: id (unique integer), title (required string), description (optional string), completed (boolean)
- **Validation**: Ensures title is not empty, id is unique, and data types are correct
- **State Management**: Tracks completion status and provides methods for state transitions

### 2. In-Memory Task Store
- **Responsibility**: Manages collection of tasks in memory with CRUD operations
- **Storage**: Uses dictionary structure with task ID as key for O(1) access
- **ID Generation**: Auto-generates unique sequential IDs for new tasks
- **Operations**: Add, retrieve, update, delete, and filter tasks
- **Persistence**: Maintains state only during application lifecycle (lost on termination)

### 3. Task Service
- **Responsibility**: Implements business logic and orchestrates operations between CLI and data layers
- **Validation**: Validates inputs before passing to data layer
- **Error Handling**: Manages error cases and provides appropriate feedback
- **Operations**: Add task, list tasks (all/completed/pending), update task, delete task, toggle completion status

### 4. Command Parser
- **Responsibility**: Interprets user commands from CLI and maps to appropriate service operations
- **Command Recognition**: Identifies available commands and validates argument structure
- **Parameter Extraction**: Parses command arguments and validates their format
- **Error Reporting**: Provides clear error messages for invalid commands or arguments

### 5. CLI Interface
- **Responsibility**: Manages user interaction loop and formatted output display
- **Input Handling**: Processes user commands and manages application flow
- **Output Formatting**: Displays tasks and messages in readable format
- **Navigation**: Provides menu options and guides user through operations

## In-Memory State Management Approach

### Storage Strategy
- **Primary Storage**: Python dictionary with integer keys mapping to task objects
- **ID Management**: Sequential ID assignment starting from 1, ensuring uniqueness
- **State Isolation**: All state exists within application memory space only
- **Access Pattern**: O(1) average time complexity for all CRUD operations

### State Consistency
- **Validation Layer**: Input validation occurs at service layer before state modification
- **Atomic Operations**: Each operation is atomic to prevent partial state changes
- **Error Recovery**: Invalid operations do not modify state, maintaining consistency
- **State Transitions**: Explicit state changes with proper validation at each step

### Memory Management
- **No Persistence**: Data exists only during application execution
- **Garbage Collection**: Relies on Python's automatic memory management
- **Size Considerations**: Designed to handle up to 100 tasks efficiently based on success criteria
- **Cleanup**: No explicit cleanup required; memory freed upon application termination

## Data Flow Between Components

### Add Task Flow
```
User Input → CLI Interface → Command Parser → Task Service → Task Store → Task Model
     ↓              ↓              ↓              ↓            ↓          ↓
  "add title"  Parse command   Validate title  Generate ID  Create    Store task
              Extract args    Create task    Assign unique   task      in memory
                              object         ID
```

### View Tasks Flow
```
User Input → CLI Interface → Command Parser → Task Service → Task Store → Format Output
     ↓              ↓              ↓              ↓            ↓          ↓
  "list all"   Parse command   Validate args   Retrieve    Get task    Display to
              Extract filter   Get tasks      tasks by     objects     user
                              from store     filter
```

### Update Task Flow
```
User Input → CLI Interface → Command Parser → Task Service → Task Store → Task Model
     ↓              ↓              ↓              ↓            ↓          ↓
  "update id    Parse command   Validate      Validate ID   Update     Return
   title"       Extract args    parameters    exists        task       success
```

### Delete Task Flow
```
User Input → CLI Interface → Command Parser → Task Service → Task Store
     ↓              ↓              ↓              ↓            ↓
  "delete id"  Parse command   Validate ID    Validate      Remove task
              Extract ID       exists         exists        from memory
```

### Mark Complete Flow
```
User Input → CLI Interface → Command Parser → Task Service → Task Store → Task Model
     ↓              ↓              ↓              ↓            ↓          ↓
  "complete id" Parse command   Validate ID    Validate      Update     Update
              Extract ID       exists         exists        status     object
```

## Mapping of CLI Commands to Operations

### Command: `add "title" ["description"]`
- **Operation**: Add New Task (FR-001)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Creates new task with unique ID, default incomplete status
- **Validation**: Title is required and non-empty
- **Output**: Confirmation with assigned ID

### Command: `list`
- **Operation**: View All Tasks (FR-002)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Retrieves and displays all tasks with ID, title, description, status
- **Validation**: No specific validation required
- **Output**: Formatted list of all tasks

### Command: `list completed`
- **Operation**: View Completed Tasks (FR-002)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Retrieves and displays completed tasks only
- **Validation**: No specific validation required
- **Output**: Formatted list of completed tasks

### Command: `list pending`
- **Operation**: View Pending Tasks (FR-002)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Retrieves and displays pending tasks only
- **Validation**: No specific validation required
- **Output**: Formatted list of pending tasks

### Command: `update <id> "new_title" ["new_description"]`
- **Operation**: Update Task (FR-003)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Modifies existing task title and/or description
- **Validation**: Task ID must exist, title must be non-empty if provided
- **Output**: Confirmation of successful update

### Command: `delete <id>`
- **Operation**: Delete Task (FR-004)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Removes task from storage
- **Validation**: Task ID must exist, user confirmation required
- **Output**: Confirmation of successful deletion

### Command: `complete <id>`
- **Operation**: Mark Task Complete (FR-005)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Updates task completion status to true
- **Validation**: Task ID must exist
- **Output**: Confirmation of status change

### Command: `incomplete <id>`
- **Operation**: Mark Task Incomplete (FR-005)
- **Component Flow**: CLI → Command Parser → Task Service → Task Store
- **Functionality**: Updates task completion status to false
- **Validation**: Task ID must exist
- **Output**: Confirmation of status change

### Command: `help`
- **Operation**: Display Help Information (FR-006)
- **Component Flow**: CLI Interface only
- **Functionality**: Shows available commands and their usage
- **Validation**: No validation required
- **Output**: Help text with command descriptions

### Command: `quit`
- **Operation**: Exit Application (FR-006)
- **Component Flow**: CLI Interface only
- **Functionality**: Terminates application gracefully
- **Validation**: No validation required
- **Output**: Exit message and application termination