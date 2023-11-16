from functools import cached_property
from pathlib import Path
from typing import Literal

import tomllib
from pydantic import MySQLDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parent.parent.parent
with open(f"{PROJECT_DIR}/pyproject.toml", "rb") as f:
    PYPROJECT_CONTENT = tomllib.load(f)["tool"]["poetry"]


class Settings(BaseSettings):
    ENVIRONMENT: Literal["LOCAL", "DEV", "PROD"] = "LOCAL"

    PROJECT_NAME: str = PYPROJECT_CONTENT["name"]
    VERSION: str = PYPROJECT_CONTENT["version"]
    DESCRIPTION: str = PYPROJECT_CONTENT["description"]

    DATABASE_HOSTNAME: str = ''
    DATABASE_USER: str = ''
    DATABASE_PASSWORD: str = ''
    DATABASE_PORT: int = 3306
    DATABASE_DB: str = ''

    @computed_field  # type: ignore
    @cached_property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return str(
            MySQLDsn.build(
                scheme="mysql+aiomysql",
                username=self.DATABASE_USER,
                password=self.DATABASE_PASSWORD,
                host=self.DATABASE_HOSTNAME,
                port=self.DATABASE_PORT,
                path=self.DATABASE_DB,
            )
        )

    model_config = SettingsConfigDict(
        env_file=f"{PROJECT_DIR}/.env", case_sensitive=True
    )


settings: Settings = Settings()
