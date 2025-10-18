from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Lazy database setup to ensure configuration is loaded before creating the engine
Base = declarative_base()

_database_url: str | None = None
_engine = None
_SessionLocal = None


def setup_database(database_url: str) -> None:
    global _database_url, _engine, _SessionLocal
    _database_url = database_url

    connect_args = {"check_same_thread": False} if _database_url.startswith("sqlite") else {}
    _engine = create_engine(_database_url, pool_pre_ping=True, pool_recycle=3600, connect_args=connect_args)
    _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_engine():
    if _engine is None:
        raise RuntimeError("Database engine has not been initialized. Call setup_database() first.")
    return _engine


def get_session_maker():
    if _SessionLocal is None:
        raise RuntimeError("Session maker not initialized. Call setup_database() first.")
    return _SessionLocal


def get_db():
    SessionLocal = get_session_maker()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()