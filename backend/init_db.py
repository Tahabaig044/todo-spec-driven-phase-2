#!/usr/bin/env python3
"""
Database initialization script for Hugging Face deployment
"""

import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from database import Base

async def init_db():
    # Use the DATABASE_URL from environment, defaulting to a file-based SQLite for simplicity
    database_url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./todo_hf.db")

    # Create async engine
    engine = create_async_engine(database_url)

    try:
        # Create all tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())