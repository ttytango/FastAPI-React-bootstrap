from .base import Settings
from pydantic import Field

class DevSettings(Settings):
    debug: bool = Field(default=True, validation_alias="DEBUG")
    
    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"
