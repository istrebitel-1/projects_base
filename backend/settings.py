import logging
import pkg_resources
from functools import lru_cache
from pathlib import Path

from pydantic import AnyHttpUrl, BaseSettings, validator


logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """App settings"""
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    APP_VERSION: str
    APP_MODE: str
    APP_CONTAINERIZED: str

    APP_LOG_LEVEL: str
    APP_LOG_PATH: str | None

    METADATA_POSTGRES_HOST: str
    METADATA_POSTGRES_PORT: str
    METADATA_POSTGRES_DATABASE: str
    METADATA_POSTGRES_USERNAME: str
    METADATA_POSTGRES_PASSWORD: str

    PGTZ: str

    JWT_ACCESS_TOKEN_SECRET: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_SIGNING_ALGORITHM: str = "HS256"

    CACHE_TIMEOUT: int = 60
    CACHE_PATH: str | Path = Path(__file__).parent.parent.resolve() / 'cache'

    def get_insensitive_configuration(self) -> dict:
        allow_variable_prefixes = (
            'CACHE_TIMEOUT',
            'PGTZ',
            'APP_',
        )

        configuration = {}
        for key, value in self.dict().items():
            if key.startswith(allow_variable_prefixes):
                configuration[key] = value

        return configuration


@lru_cache()
def get_settings() -> Settings:
    return Settings(
        APP_VERSION=pkg_resources.get_distribution("project-base").version,
    )
