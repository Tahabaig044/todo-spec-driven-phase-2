---
title: Todo API
emoji: 📝
colorFrom: blue
colorTo: indigo
sdk: docker
dockerfile: Dockerfile.hf
pinned: false
license: mit
---

# Todo API Backend

This is a FastAPI-based Todo application backend deployed on Hugging Face Spaces.

## API Endpoints

- `GET /` - Root endpoint
- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{task_id}` - Get a specific task
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task

## Environment Variables

- `DATABASE_URL` - Database connection string (PostgreSQL recommended)

## Local Development

To run this application locally:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Tech Stack

- FastAPI - Web framework
- SQLAlchemy - ORM
- AsyncPG - PostgreSQL driver
- Uvicorn - ASGI server

## License

MIT