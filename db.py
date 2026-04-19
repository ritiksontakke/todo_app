import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Database connection and session management
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Create async engine for PostgreSQL
# pool_size controls how many connections to keep open
# max_overflow allows temporary connections beyond pool_size
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Log SQL queries in debug mode
    pool_size=5,          # Maintain 5 connections in the pool
    max_overflow=10,      # Allow up to 10 additional connections
    pool_pre_ping=True,   # Verify connections before use
)

# Session factory for creating database sessions
# expire_on_commit=False prevents attribute access issues after commit
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base class for all SQLAlchemy models
Base = declarative_base()

async def get_db():
    """
    Dependency that provides a database session.
    Automatically closes the session when the request completes.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()