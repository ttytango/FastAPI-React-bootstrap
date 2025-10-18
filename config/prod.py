from .base import Settings
from pydantic import Field

class ProdSettings(Settings):
    debug: bool = Field(default=False, validation_alias="DEBUG")
    
    class Config:
        env_file = ".env.prod"
        env_file_encoding = "utf-8"