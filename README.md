# Todo Application - Full-Stack Web Application (Phase 2)

This is a full-stack todo application built with Next.js (frontend) and FastAPI (backend) with PostgreSQL database. Phase 1 CLI functionality is preserved and maintained.

## Project Structure

```
todo-spec-driven/
├── frontend/                 # Next.js frontend application
│   ├── app/                 # Next.js app router
│   ├── components/          # React components
│   ├── types/              # TypeScript type definitions
│   ├── services/           # API service
│   └── context/            # React Context
├── backend/                # FastAPI backend application
│   ├── api/               # API routes
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── database/          # Database configuration
│   ├── services/          # Business logic
│   └── crud/              # Database operations
├── specs/                 # Project specifications
└── src/                   # Phase 1 CLI application (preserved)
```

## Prerequisites

- Node.js 18+ and npm
- Python 3.13+
- PostgreSQL (for local development) or Neon account (for cloud)

## Local Development Setup

### Option 1: Using Docker (Recommended)

1. Make sure you have Docker and Docker Compose installed
2. Run the application:
   ```bash
   docker-compose up --build
   ```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend API Documentation: http://localhost:8000/docs

### Option 2: Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   # Create a PostgreSQL database (using Neon or local PostgreSQL)
   # Copy .env.example to .env and update with your database URL
   cp .env.example .env
   # Edit .env with your database connection string
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a .env.local file:
   ```bash
   # For local development
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   ```

4. Start the frontend:
   ```bash
   npm run dev
   ```

The frontend will be available at http://localhost:3000

## Features

- Add, view, update, delete, and mark tasks as complete
- Responsive web UI built with Next.js and Tailwind CSS
- REST API with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Real-time task management
- Filtering by completion status
- Task editing functionality

## API Endpoints

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{id}` - Get a specific task
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task

## Phase 1 CLI Application (Preserved)

The original Phase 1 CLI application is preserved in the `src/` directory and can be run with:
```bash
python main.py
```

### Phase 1 CLI Features

- Add, view, update, delete, and mark tasks as complete/incomplete
- In-memory storage (no persistence)
- Command-line interface
- Task filtering by completion status

### Phase 1 CLI Commands

#### Add a Task
```
add "title" ["description"]
```
Add a new task with a required title and optional description.

Example:
```
add "Buy groceries" "Milk, bread, eggs"
```

#### List Tasks
```
list
```
List all tasks with their ID, title, description, and status.

#### List Completed Tasks
```
list completed
```
List only completed tasks.

#### List Pending Tasks
```
list pending
```
List only pending tasks.

#### Update a Task
```
update <id> "new_title" ["new_description"]
```
Update the title and/or description of an existing task.

Example:
```
update 1 "Updated title" "Updated description"
```

#### Mark Task as Complete
```
complete <id>
```
Mark a task as complete.

Example:
```
complete 1
```

#### Mark Task as Incomplete
```
incomplete <id>
```
Mark a completed task as incomplete.

Example:
```
incomplete 1
```

#### Delete a Task
```
delete <id>
```
Remove a task from the system.

Example:
```
delete 1
```

#### Help
```
help
```
Show available commands and their usage.

#### Quit
```
quit
```
Exit the application.

## Architecture

- Frontend: Next.js 14 with App Router, TypeScript, Tailwind CSS
- Backend: FastAPI with Pydantic, SQLAlchemy ORM, PostgreSQL
- Database: PostgreSQL (with Neon support)
- Communication: REST API with JSON
- Phase 1: Python 3.13+ CLI application with clean architecture

## Development

The project follows a clean architecture with clear separation between frontend and backend components. All changes maintain compatibility with Phase 1 functionality.

## Deployment

For deployment to cloud platforms:
- Frontend: Deploy to Vercel, Netlify, or similar
- Backend: Deploy to Railway, Render, or similar
- Database: Use Neon PostgreSQL hosting