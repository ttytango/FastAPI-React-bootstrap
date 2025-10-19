import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.responses import JSONResponse

from config import configure, get_settings
from authentication_service.routers.auth import router as auth_router
from authentication_service.routers.users import router as users_router
from db import Base, setup_database, get_engine


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    import models.user  # ensure models registered
    Base.metadata.create_all(bind=get_engine())
    yield


app = FastAPI(lifespan=lifespan, title="Authentication Service")


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    msgs = [e.get("msg", "Invalid input") for e in exc.errors()]
    msg = "; ".join(msgs)
    if msg.startswith("Value error, "):
        msg = msg[len("Value error, "):]
    logger.warning("422 %s -> %s", request.url.path, msg)
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": msg})


configure()
settings = get_settings()
setup_database(settings.database_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"service": "auth", "env": settings.environment, "debug": settings.debug}


@app.get("/healthcheck")
async def read_status():
    return {"status": "ok"}


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])


