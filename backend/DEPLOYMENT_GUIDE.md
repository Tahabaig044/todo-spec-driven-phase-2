# Hugging Face Spaces Deployment Guide

## Files Created

1. **Dockerfile.hf** - Optimized Dockerfile for Hugging Face Spaces deployment
2. **space.yaml** - Hugging Face Spaces configuration
3. **README.md** - Space metadata and documentation
4. **init_db.py** - Database initialization script
5. **start.sh** - Startup script with database initialization
6. **Updated main.py** - With Hugging Face environment variable support

## Deployment Steps

### Option 1: Direct Upload to Hugging Face Spaces

1. Create a new Space on Hugging Face:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Docker" SDK
   - Choose CPU hardware
   - Upload all files from the backend directory

2. Or create from a Git repository:
   - Fork this repository to your GitHub account
   - Link your GitHub account to Hugging Face
   - Create a Space and point it to your forked repository
   - Make sure to include the Dockerfile.hf in your repository root (rename it to Dockerfile if needed)

### Option 2: Using Git CLI

1. Clone your Space repository:
```bash
git clone https://huggingface.co/spaces/[your-username]/[space-name]
cd [space-name]
```

2. Copy the backend files:
```bash
cp -r /path/to/backend/* .
```

3. Use the Dockerfile.hf as your Dockerfile (rename if needed):
```bash
cp Dockerfile.hf Dockerfile
```

4. Commit and push:
```bash
git add .
git commit -m "Add Todo API backend"
git push origin main
```

## Environment Variables

Set the following secrets in your Hugging Face Space settings:

- `DATABASE_URL` - PostgreSQL connection string (e.g., `postgresql+asyncpg://username:password@host:port/database`)

For development/testing, you can use SQLite:
- `DATABASE_URL=sqlite+aiosqlite:///./todo_hf.db`

## API Endpoints

Once deployed, your API will be available at:
- `https://[your-username]-[space-name].hf.space/`
- Health check: `https://[your-username]-[space-name].hf.space/health`
- API endpoints: `https://[your-username]-[space-name].hf.space/api/...`

## Features

- FastAPI backend with async support
- SQLAlchemy ORM with async drivers
- Automatic database initialization
- Health check endpoint
- Proper CORS configuration
- Environment variable support for configuration

## Troubleshooting

1. If the Space fails to build, check the build logs in the Space settings
2. If the application crashes, check the runtime logs
3. Make sure your DATABASE_URL is properly configured
4. For PostgreSQL, ensure the connection string format is correct

## Scaling

For production use, consider:
- Using a managed PostgreSQL database instead of SQLite
- Adding connection pooling configuration
- Implementing proper logging
- Adding monitoring and alerting