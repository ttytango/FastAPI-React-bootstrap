from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import configure, get_settings
from routers.auth import router as auth_router
from routers.users import router as users_router
from db import Base, setup_database, get_engine

app = FastAPI()

configure()
settings = get_settings()
setup_database(settings.database_url)

origins = settings.cors_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    # Ensure all SQLAlchemy models are registered before this import
    # Import models so they are registered with Base metadata
    import models.user  # noqa: F401
    Base.metadata.create_all(bind=get_engine())

@app.get("/")
async def root():
    return {"message": "Hello World", "env": settings.environment, "debug": settings.debug}


@app.get("/healthcheck")
async def read_status():
    return {"status": "ok"}


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])