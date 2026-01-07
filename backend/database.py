from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL - defaults to a local SQLite database for development
# For PostgreSQL with asyncpg, use: postgresql+asyncpg://user:pass@localhost/dbname
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./todo_test.db")

# Determine if we're using SQLite (doesn't support pool_size/max_overflow)
if "sqlite" in DATABASE_URL:
    # SQLite doesn't support pool_size and max_overflow
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,  # Set to False in production
        pool_pre_ping=True
    )
else:
    # PostgreSQL supports pool configurations
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,  # Set to False in production
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10
    )

# Create async session maker
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for declarative models
Base = declarative_base()

# Dependency to get DB session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session