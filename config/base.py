import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
from enum import Enum, IntEnum

from pydantic import BaseModel

class Status(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
     
class Role(str, Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"
    contributor = "contributor"
    viewer = "viewer"
    
class Permission(str, Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    role: Role


def set_database_url(url: str):
    load_dotenv()
    global DATABASE_URL
    DATABASE_URL = url
    os.environ["DATABASE_URL"] = DATABASE_URL
    


def get_database_url() -> str:
    load_dotenv()
    url = os.getenv("DATABASE_URL", None)
    if not url:
        raise ValueError("DATABASE_URL is not set")
    return url

class Settings(BaseSettings):
    app_name: str = "FastAPI"
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")
    database_url: str = Field(default=get_database_url(), validation_alias="DATABASE_URL")
    # database_url: str = Field(default=, validation_alias="DATABASE_URL")
    cors_origins: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:5173"], validation_alias="CORS_ORIGINS"
    )
    debug: bool = Field(default=False, validation_alias="DEBUG")

    # JWT / Auth
    jwt_secret_key: str = Field(default="change-me", validation_alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", validation_alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=60, validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES")


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
