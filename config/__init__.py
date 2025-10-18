import os
from typing import Optional

from .base import Settings
from .dev import DevSettings
from .prod import ProdSettings

_settings: Settings | None = None

def configure(environment: Optional[str] = None) -> Settings:
    """Configure and return the active settings instance based on environment."""
    global _settings
    env = (environment or os.getenv("ENVIRONMENT") or "development").lower()

    if env in ("dev", "development", "local"):
        _settings = DevSettings()
    elif env in ("prod", "production"):
        _settings = ProdSettings()
    else:
        _settings = DevSettings()

    return _settings

def get_settings() -> Settings:
    """Return the active settings instance, configuring it if needed."""
    if _settings is None:
        return configure()
    return _settings