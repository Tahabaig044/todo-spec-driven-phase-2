# Todo Application - Phase 2 Specification: Full-Stack Web Application

## Feature Overview

A full-stack web application that extends the existing console-based Todo application with a modern web interface and persistent database storage. The application will maintain all Phase 1 functionality while adding a responsive web UI, REST API, and PostgreSQL database integration.

## User Scenarios & Testing

### Scenario 1: Web UI Access
- User navigates to the application URL
- User sees a responsive web interface with task management capabilities
- User can interact with the application using standard web UI patterns

### Scenario 2: Adding a New Task (Web UI)
- User sees an "Add Task" form with title and description fields
- User enters task details and clicks "Add Task"
- System creates the task and displays it in the task list
- Task appears with a unique ID and is marked as incomplete

### Scenario 3: Viewing Tasks (Web UI)
- User sees all tasks displayed in a clean, organized list
- Tasks are visually differentiated by completion status (completed vs incomplete)
- User can sort tasks by various criteria (ID, title, status, creation date)
- Pagination is available for large task lists

### Scenario 4: Updating a Task (Web UI)
- User clicks an "Edit" button on a specific task
- An edit form appears with current task details
- User modifies the title, description, or completion status
- User saves changes, which are reflected immediately in the UI

### Scenario 5: Deleting a Task (Web UI)
- User clicks a "Delete" button on a specific task
- A confirmation dialog appears to prevent accidental deletion
- User confirms deletion, and the task is removed from the list
- Appropriate feedback is provided to confirm the action

### Scenario 6: Marking Task Complete (Web UI)
- User clicks a checkbox or "Mark Complete" button on a task
- Task status updates immediately in the UI
- Task visually moves to the completed section or updates its appearance
- System updates the task status in the database

### Scenario 7: API Integration
- Web UI communicates with backend through REST API endpoints
- All operations are performed via API calls
- Real-time updates are reflected in the UI without page refresh

## Functional Requirements

### FR-001: Web UI - Add New Task
- **Requirement**: The web UI shall provide a form to add new tasks
- **Inputs**: Task title (required), task description (optional)
- **Processing**: UI sends data to REST API which creates a new record in PostgreSQL
- **Output**: New task appears in the task list with unique ID and completion status
- **Acceptance Criteria**:
  - [ ] Form includes validation for required fields
  - [ ] Form submission is disabled during API call
  - [ ] Success/error messages are displayed appropriately
  - [ ] Task appears immediately in the task list after creation
  - [ ] Form resets after successful submission

### FR-002: Web UI - View Tasks
- **Requirement**: The web UI shall display all tasks with filtering and sorting capabilities
- **Inputs**: None required (initial load), optional filter/sort parameters
- **Processing**: UI fetches tasks from REST API and renders them in an organized list
- **Output**: List of tasks with ID, title, description, and completion status
- **Acceptance Criteria**:
  - [ ] All tasks are displayed with clear visual indicators
  - [ ] Tasks are grouped by completion status (completed/incomplete)
  - [ ] Sorting options are available (by ID, title, creation date)
  - [ ] Filtering options are available (all/completed/incomplete)
  - [ ] Empty state is handled gracefully with appropriate messaging

### FR-003: Web UI - Update Task
- **Requirement**: The web UI shall allow users to modify existing tasks
- **Inputs**: Task ID, new title (optional), new description (optional), completion status (optional)
- **Processing**: UI sends update request to REST API which modifies the database record
- **Output**: Updated task is reflected in the UI with success confirmation
- **Acceptance Criteria**:
  - [ ] Task ID must exist in the system
  - [ ] User can update title without changing other fields
  - [ ] User can update description without changing other fields
  - [ ] User can toggle completion status independently
  - [ ] System provides visual feedback during update process
  - [ ] Invalid inputs are handled gracefully with validation

### FR-004: Web UI - Delete Task
- **Requirement**: The web UI shall allow users to remove tasks with confirmation
- **Inputs**: Task ID
- **Processing**: UI sends delete request to REST API which removes the database record
- **Output**: Task is removed from the UI with confirmation message
- **Acceptance Criteria**:
  - [ ] Task ID must exist in the system
  - [ ] Confirmation dialog prevents accidental deletion
  - [ ] Task is completely removed from the UI and database
  - [ ] System provides appropriate feedback after deletion
  - [ ] Invalid task IDs are handled gracefully

### FR-005: Web UI - Mark Task Complete/Incomplete
- **Requirement**: The web UI shall allow users to toggle task completion status
- **Inputs**: Task ID
- **Processing**: UI sends status update to REST API which updates the database record
- **Output**: Task status is updated in the UI with visual feedback
- **Acceptance Criteria**:
  - [ ] Task ID must exist in the system
  - [ ] Task completion status is toggled in real-time
  - [ ] Visual representation updates immediately
  - [ ] System provides appropriate feedback
  - [ ] Invalid task IDs are handled gracefully

### FR-006: REST API - Create Task Endpoint
- **Requirement**: The backend shall provide a REST endpoint to create new tasks
- **Endpoint**: `POST /api/tasks`
- **Request Body**: JSON object with `title` (required) and `description` (optional)
- **Response**: JSON object with created task data and HTTP 201 status
- **Acceptance Criteria**:
  - [ ] Validates required fields are present
  - [ ] Creates task in PostgreSQL database
  - [ ] Returns complete task object with assigned ID
  - [ ] Sets completion status to false by default
  - [ ] Returns appropriate error responses for validation failures

### FR-007: REST API - Get All Tasks Endpoint
- **Requirement**: The backend shall provide a REST endpoint to retrieve all tasks
- **Endpoint**: `GET /api/tasks`
- **Query Parameters**: `status` (optional: all/completed/incomplete), `sort` (optional: id/title/date)
- **Response**: JSON array of task objects with HTTP 200 status
- **Acceptance Criteria**:
  - [ ] Returns all tasks when no filters applied
  - [ ] Filters by completion status when parameter provided
  - [ ] Sorts results by specified criteria
  - [ ] Handles empty database gracefully
  - [ ] Includes pagination when applicable

### FR-008: REST API - Get Task by ID Endpoint
- **Requirement**: The backend shall provide a REST endpoint to retrieve a specific task
- **Endpoint**: `GET /api/tasks/{id}`
- **Response**: JSON object with task data or 404 if not found
- **Acceptance Criteria**:
  - [ ] Returns specific task when ID exists
  - [ ] Returns 404 error when task ID doesn't exist
  - [ ] Returns complete task object with all fields

### FR-009: REST API - Update Task Endpoint
- **Requirement**: The backend shall provide a REST endpoint to update existing tasks
- **Endpoint**: `PUT /api/tasks/{id}`
- **Request Body**: JSON object with optional `title`, `description`, `completed` fields
- **Response**: JSON object with updated task data or 404 if not found
- **Acceptance Criteria**:
  - [ ] Updates only provided fields, leaves others unchanged
  - [ ] Validates task exists before updating
  - [ ] Returns updated task object
  - [ ] Returns 404 when task ID doesn't exist
  - [ ] Returns appropriate error responses for validation failures

### FR-010: REST API - Delete Task Endpoint
- **Requirement**: The backend shall provide a REST endpoint to delete tasks
- **Endpoint**: `DELETE /api/tasks/{id}`
- **Response**: Empty body with HTTP 204 status or 404 if not found
- **Acceptance Criteria**:
  - [ ] Removes task from database when ID exists
  - [ ] Returns 204 status on successful deletion
  - [ ] Returns 404 when task ID doesn't exist
  - [ ] Handles deletion gracefully without errors

### FR-011: Database Integration
- **Requirement**: The backend shall use PostgreSQL database with Neon for task storage
- **Processing**: All task operations shall be persisted to and retrieved from database
- **Acceptance Criteria**:
  - [ ] Tasks persist between application sessions
  - [ ] Data integrity is maintained
  - [ ] Database schema matches task entity definition
  - [ ] Proper indexing for efficient queries
  - [ ] Connection pooling for performance

## Database Schema

### Tasks Table
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Indexes
- Primary key index on `id`
- Index on `completed` field for efficient filtering
- Index on `created_at` for sorting by creation date

## REST API Specification

### Base URL
`/api/`

### Authentication
- No authentication required for Phase 2 (single-user application)

### Common Response Format
Success responses: `200 OK` with JSON body
Error responses: Appropriate HTTP status code with JSON error object:
```json
{
  "error": "Error message",
  "code": "error_code",
  "details": {}
}
```

### Endpoints Summary
- `POST /api/tasks` - Create new task
- `GET /api/tasks` - Get all tasks with optional filters
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update specific task
- `DELETE /api/tasks/{id}` - Delete specific task

## Validation and Error Handling

### Input Validation
- Task title: Required, string, max 255 characters
- Task description: Optional, string, max 1000 characters
- Task ID: Must be a positive integer
- Task completion: Must be boolean value

### Error Responses
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Task ID does not exist
- `422 Unprocessable Entity`: Validation errors
- `500 Internal Server Error`: Server-side errors

### Error Handling Patterns
- All API endpoints return consistent error format
- Frontend displays user-friendly error messages
- Validation errors include specific field information
- Network errors are handled gracefully with retry options

## User Experience Flows

### Create Task Flow
1. User sees "Add Task" button/form
2. User fills in title (and optional description)
3. User clicks "Add Task" button
4. Form shows loading state
5. Task appears in list with success feedback
6. Form resets for next entry

### Edit Task Flow
1. User clicks "Edit" on a task
2. Edit form appears with current values
3. User modifies fields as needed
4. User clicks "Save" button
5. Form shows loading state
6. Task updates in list with success feedback
7. Edit form closes

### List Tasks Flow
1. Application loads and fetches tasks
2. Tasks are displayed in organized list
3. User can filter/sort using available controls
4. Completed and incomplete tasks are visually separated
5. Empty state is shown when no tasks exist

### Delete Task Flow
1. User clicks "Delete" on a task
2. Confirmation dialog appears
3. User confirms deletion
4. Task removal shows loading state
5. Task disappears from list with success feedback

## Non-Functional Requirements

### Performance
- API endpoints respond within 500ms for up to 10,000 tasks
- Web UI renders task list within 1 second for up to 1,000 tasks
- Database queries execute within 100ms for common operations
- Page load time under 2 seconds with normal network conditions

### Security
- Input validation to prevent SQL injection
- Proper escaping of user content to prevent XSS
- Secure API endpoints with appropriate error handling
- No sensitive data stored in client-side storage

### Scalability
- Database schema supports up to 100,000 tasks
- API endpoints handle concurrent requests appropriately
- Frontend manages state efficiently to prevent memory leaks
- Connection pooling for database operations

### Reliability
- 99% uptime for API endpoints
- Graceful degradation when database is unavailable
- Proper error handling and logging
- Consistent data integrity across operations

### Maintainability
- Clean separation between frontend and backend
- Well-documented API endpoints
- Consistent code structure and naming conventions
- Comprehensive error logging for debugging

### Compatibility
- Modern web browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for mobile and desktop
- REST API compatible with standard HTTP clients

## Assumptions

- Users have access to a modern web browser
- Network connectivity is available for API communication
- PostgreSQL database (Neon) is properly configured and accessible
- Application runs in a web server environment
- Single-user application (no concurrent multi-user support needed)

## Constraints

- Phase 1 CLI functionality must remain intact alongside web interface
- No AI features to be implemented in this phase
- REST API only (no GraphQL in Phase 2)
- Next.js for frontend, FastAPI for backend
- PostgreSQL database with Neon hosting
- No authentication/authorization required for Phase 2