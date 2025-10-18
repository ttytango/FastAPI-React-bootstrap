import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

# DATABASE_URL="mysql+pymysql://user:pass@localhost:3306/mydb?charset=utf8mb4"


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


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
